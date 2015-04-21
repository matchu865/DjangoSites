# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.hostname = "FinalProject"
  # config.vm.box = "ubuntu/trusty64"
  config.vm.box = "GR360RY/trusty64-desktop-minimal"
  config.vm.network "private_network", ip: "192.168.33.2"
  config.ssh.forward_agent = "true"
  config.ssh.forward_x11 = "true"
  config.vm.provision "shell",
    inline:  "apt-get -y update"
  config.vm.provider "virtualbox" do |vb|
    vb.name = "FinalProject"
     vb.gui = true
     vb.customize ["modifyvm", :id, "--memory", "1000"]
     vb.customize ["modifyvm", :id, "--cpus", "2"]
   end
end
