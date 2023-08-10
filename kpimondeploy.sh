OAIC=`pwd`
sudo apt-get install nginx
          
sudo systemctl start nginx.service
cd /etc/nginx/sites-enabled
sudo unlink default
cd ../
cd ../../var/www
sudo mkdir xApp_config.local
cd xApp_config.local/
sudo mkdir config_files
cd ../../../etc/nginx/conf.d
sudo sh -c "echo 'server {
listen 5010 default_server;
server_name xApp_config.local;
location /config_files/ {
root /var/www/xApp_config.local/;
}
}' >xApp_config.local.conf"

echo ">>> reloading nginx..."
sudo nginx -t 
cd ${OAIC}
sudo cp ric-scp-kpimon/scp-kpimon-config-file.json /var/www/xApp_config.local/config_files/
sudo systemctl reload nginx


echo ">>> getting machine IP..."
export MACHINE_IP=`hostname  -I | cut -f1 -d' '`

echo ">>> checking for config-file"
curl http://${MACHINE_IP}:5010/config_files/scp-kpimon-config-file.json
echo ">>> building docker image...."
cd ${OAIC}/ric-scp-kpimon
echo ">>> checking directory"
ls
sudo docker build . -t xApp-registry.local:5008/scp-kpimon:1.0.1

export KONG_PROXY=`sudo kubectl get svc -n ricplt -l app.kubernetes.io/name=kong -o jsonpath='{.items[0].spec.clusterIP}'`
export APPMGR_HTTP=`sudo kubectl get svc -n ricplt --field-selector metadata.name=service-ricplt-appmgr-http -o jsonpath='{.items[0].spec.clusterIP}'`
export ONBOARDER_HTTP=`sudo kubectl get svc -n ricplt --field-selector metadata.name=service-ricplt-xapp-onboarder-http -o jsonpath='{.items[0].spec.clusterIP}'`
          
echo "KONG_PROXY = $KONG_PROXY"
echo "APPMGR_HTTP = $APPMGR_HTTP"
echo "ONBOARDER_HTTP = $ONBOARDER_HTTP"

echo ">>> getting charts..."
curl --location --request GET "http://$KONG_PROXY:32080/onboard/api/v1/charts"
ls
echo '{"config-file.json_url":"http://'$MACHINE_IP':5010/config_files/scp-kpimon-config-file.json"}' > scp-kpimon-onboard.url
          
echo ">>> scp-kpimon-onboard.url"
cat scp-kpimon-onboard.url
echo ">>> curl POST..."
curl -L -X POST "http://$KONG_PROXY:32080/onboard/api/v1/onboard/download" --header 'Content-Type: application/json' --data-binary "@scp-kpimon-onboard.url"

echo ">>> curl GET..."
curl -L -X GET "http://$KONG_PROXY:32080/onboard/api/v1/charts"
echo ">>> curl POST..."
curl -L -X POST "http://$KONG_PROXY:32080/appmgr/ric/v1/xapps" --header 'Content-Type: application/json' --data-raw '{"xappName": "scp-kpimon"}'
          
#sleep 10

#echo ">>> getting pods..."
#sudo kubectl get pods -A | grep 'kpimon' | grep 'Running'
#echo ">>> showing kubernetes logs..."
  
#sudo timeout 5 sudo kubectl logs -f -n ricxapp -l app=ricxapp-scp-kpimon || rc=$?
#rc=$? #124 for succesful ping
#if [ $rc -ne 124 ] ; then exit -1 ; fi
#sudo kubectl logs -f -n ricxapp -l app=ricxapp-scp-kpimon
          
#echo ">>> printing decoded metrics..."
#sudo timeout 5 sudo kubectl exec -it -n ricxapp `sudo kubectl get pod -n ricxapp -l app=ricxapp-scp-kpimon -o jsonpath='{.items[0].metadata.name}'` -- tail -F /opt/kpimon.log || rc=$?
#if [ $rc -ne 124 ] ; then exit -1 ; fi
          
echo 'Successful: KPIMON xApp up and running'
