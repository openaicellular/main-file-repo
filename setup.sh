#!/usr/bin/env bash

#install dependencies
apt-get install git build-essential cmake libfftw3-dev libmbedtls-dev libboost-program-options-dev libconfig++-dev libsctp-dev libtool autoconf -y

#clone oaic repo and pull submodules
git clone https://github.com/joshuamoorexyz/oaic-testing.git
cd oaic-testing

#export $rootdir="${pwd/}"

#echo $rootdir
#Near real time RIC installation
cd RIC-Deployment/tools/k8s/bin
./gen-cloud-init.sh
./k8s-1node-cloud-init-k_1_16-h_2_17-d_cur.sh #do we need to restart?


#influxdb setup
kubectl get ns ricinfra
kubectl create ns ricinfra
helm install stable/nfs-server-provisioner --namespace ricinfra --name nfs-release-1
kubectl patch storageclass nfs -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
apt install nfs-common


#modified E2 docker image
sudo docker run -d -p 5001:5000 --restart=always --name ric registry:2


cd ~/
cd oaicinstaller
cd oaic-testing
cd /ric-plt-e2/
cd RIC-E2-TERMINATION
docker build -f Dockerfile -t localhost:5001/ric-plt-e2:5.5.0 .
docker push localhost:5001/ric-plt-e2:5.5.0
cd ~/
cd oaicinstaller
cd oaic-testing


#Near real time ric
cd RIC-Deployment/bin
./deploy-ric-platform -f ../RECIPE_EXAMPLE/PLATFORM/example_recipe_oran_e_release.yaml
cd ~/
cd oaicinstaller
cd oaic-testing

#srsRAN with E2 installation
apt-get install libzmq3-dev
add-apt-repository ppa:ettusresearch/uhd
apt-get update
apt-get install libuhd-dev libuhd4.1.0 uhd-hos


#asn1c Compiler installation
git clone https://gitlab.eurecom.fr/oai/asn1c.git
cd asn1c
git checkout velichkov_s1ap_plus_option_group
autoreconf -iv
./configure
make -j`nproc`
make install
ldconfig
cd ~/
cd oaicinstaller
cd oaic-testing


cd srsRAN-e2
mkdir build
export SRS=`realpath .`
cd build
cmake ../ -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DRIC_GENERATED_E2AP_BINDING_DIR=${SRS}/e2_bindings/E2AP-v01.01 \
    -DRIC_GENERATED_E2SM_KPM_BINDING_DIR=${SRS}/e2_bindings/E2SM-KPM \
    -DRIC_GENERATED_E2SM_GNB_NRT_BINDING_DIR=${SRS}/e2_bindings/E2SM-GNB-NRT
make -j`nproc`
make test
sudo make install
sudo ldconfig
srsran_install_configs.sh user --force
cd ~/
cd oaicinstaller
cd oaic-testing

