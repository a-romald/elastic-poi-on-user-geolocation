Vagrant.configure("2") do |config|

  config.vm.box = "bento/ubuntu-16.04"

  config.vm.hostname = "webdev"

  config.vm.network "private_network", ip: "192.168.33.10"

  # sync: folder (host machine) -> folder '/vagrant' (guest machine)
  config.vm.synced_folder './', '/vagrant', owner: 'vagrant', group: 'vagrant'

  config.vm.provision "shell", path: "provision.sh"

end