git clone https://github.com/openaicellular/oaict-test-xapp
sudo apt update
sudo apt install -y python3-pip
sudo pip3 install configparser
sudo pip3 install psutil configparser

sudo cp oaict-test-xapp/sc3-config-file.json /var/www/xApp_config.local/config_files/
sudo systemctl reload nginx

cd oaict-test-xapp/
echo ">>> getting machine IP..."
export MACHINE_IP=`hostname  -I | cut -f1 -d' '`

echo ">>> checking for config-file"
curl http://${MACHINE_IP}:5010/config_files/sc3-config-file.json

echo ">>> building docker image...."

echo ">>> checking directory"
ls
sudo docker build . -t xApp-registry.local:5008/sc3:0.0.1

sleep 20

export KONG_PROXY=`sudo kubectl get svc -n ricplt -l app.kubernetes.io/name=kong -o jsonpath='{.items[0].spec.clusterIP}'`
export APPMGR_HTTP=`sudo kubectl get svc -n ricplt --field-selector metadata.name=service-ricplt-appmgr-http -o jsonpath='{.items[0].spec.clusterIP}'`
export ONBOARDER_HTTP=`sudo kubectl get svc -n ricplt --field-selector metadata.name=service-ricplt-xapp-onboarder-http -o jsonpath='{.items[0].spec.clusterIP}'`

echo "KONG_PROXY = $KONG_PROXY"
echo "APPMGR_HTTP = $APPMGR_HTTP"
echo "ONBOARDER_HTTP = $ONBOARDER_HTTP"

echo ">>> getting charts..."
curl --location --request GET "http://$KONG_PROXY:32080/onboard/api/v1/charts"
ls
echo '{"config-file.json_url":"http://'$MACHINE_IP':5010/config_files/sc3-config-file.json"}' > sc3-onboard.url

echo ">>> sc3-onboard.url"
cat scp-kpimon-onboard.url
echo ">>> curl POST..."
curl -L -X POST "http://$KONG_PROXY:32080/onboard/api/v1/onboard/download" --header 'Content-Type: application/json' --data-binary "@sc3-onboard.url"



o ">>> curl GET..."
curl -L -X GET "http://$KONG_PROXY:32080/onboard/api/v1/charts"
echo ">>> curl POST..."
curl -L -X POST "http://$KONG_PROXY:32080/appmgr/ric/v1/xapps" --header 'Content-Type: application/json' --data-raw '{"xappName": "sc3"}'

#sleep 10

#echo ">>> getting pods..."
#sudo kubectl get pods -A | grep 'sc3' | grep 'Running'
#echo ">>> showing kubernetes logs..."


#sudo timeout 5 sudo kubectl exec -it -n ricxapp `sudo kubectl get pod -n ricxapp -l app=ricxapp-sc3 -o jsonpath='{.items[0].metadata.name}'` -- tail -F /opt/sc3.log || rc=$?
#if [ $rc -ne 124 ] ; then exit -1 ; fi

echo "oaict-xApp successfullyy installed!..."
