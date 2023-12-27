Vagrant.configure("2") do |k8s_lab|
    k8s_lab.vm.define "worker01" do |worker01|
       worker01.vm.provider "virtualbox" do |v|
          v.cpus = 2
          v.memory = 4096
       end
       worker01.vm.box = "generic/rocky8"
       worker01.vm.hostname = "worker01.9prints.internal"
       worker01.vm.network "private_network", ip: "192.168.56.101"
       worker01.vm.network "forwarded_port", id: "ssh", host: 2201, guest: 22
    #    worker01.vm.synced_folder ".", "/vagrant"
       end
    k8s_lab.vm.define "worker02" do |worker02|
       worker02.vm.provider "virtualbox" do |v|
          v.cpus = 2
          v.memory = 4096
       end
       worker02.vm.box = "generic/rocky8"
       worker02.vm.hostname = "worker02.9prints.internal"
       worker02.vm.network "private_network", ip: "192.168.56.102"
       worker02.vm.network "forwarded_port", id: "ssh", host: 2202, guest: 22
    #    worker02.vm.synced_folder ".", "/vagrant"
       end
    k8s_lab.vm.define "worker03" do |worker03|
        worker03.vm.provider "virtualbox" do |v|
           v.cpus = 2
           v.memory = 4096
        end
        worker03.vm.box = "generic/ubuntu1804"
        worker03.vm.hostname = "worker03.9prints.internal"
        worker03.vm.network "private_network", ip: "192.168.56.103"
        worker03.vm.network "forwarded_port", id: "ssh", host: 2203, guest: 22
        # worker03.vm.synced_folder ".", "/vagrant"
        end
 end
 
 