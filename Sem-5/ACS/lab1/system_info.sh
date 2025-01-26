get_os_info() {
    os_name=$(grep "NAME" /etc/os-release | head -1 | cut -d '=' -f 2)
    os_version=$(grep "VERSION" /etc/os-release | sed -n '2p' | awk -F'"' '{print $2}')
    kernel_version=$(uname -r)
    kernel_architecture=$(uname -m)

    echo "Operating System: $os_name"
    echo "OS Version: $os_version"
    echo "Kernel Version: $kernel_version"
    echo "Kernel Architecture: $kernel_architecture"
}

get_cpu_info() {
    cpu_model=$(grep "model name" /proc/cpuinfo | head -1 | cut -d ':' -f 2 | xargs)
    cpu_frequency=$(grep "cpu MHz" /proc/cpuinfo | head -1 | cut -d ':' -f 2 | xargs)
    cpu_cores=$(grep "cpu cores" /proc/cpuinfo | head -1 | cut -d ':' -f 2 | xargs)
    cpu_cache=$(lscpu -C | tail -n +2 | awk '{print "Name: ", $1, "Size: ", $2}')
    cpu_count=$(grep -c "physical id" /proc/cpuinfo)

    echo "CPU Model: $cpu_model"
    echo "CPU Frequency: $cpu_frequency MHz"
    echo "Number of Cores: $cpu_cores"
    echo "Number of CPUs: $cpu_count"
    echo "Cache:" 
    echo "$cpu_cache"
}

get_memory_info() {
    total_memory=$(free -m | grep Mem | awk '{print $2}')
    available_memory=$(free -m | grep Mem | awk '{print $7}')
    used_memory=$((total_memory - available_memory))

    echo "Total Memory: $total_memory MB"
    echo "Available Memory: $available_memory MB"
    echo "Used Memory: $used_memory MB"
}

get_network_info() {
    interfaces=$(ip -o link show | awk -F': ' '{print $2}')
    for iface in $interfaces; do
        ip_addrs=$(ip -o -4 addr show "$iface" | awk '{printf " %s", $4}')
        mac_addr=$(ip link show "$iface" | grep link/ether | awk '{print $2}')
        speed=$(cat /sys/class/net/"$iface"/speed 2>/dev/null || nix run nixpkgs#iw "$iface" link | grep rx | awk '{print $3}')

        echo "Interface: $iface"
        echo "IP Addresses:$ip_addrs"
        echo "MAC Address: ${mac_addr:-Unknown}"
        echo "Speed: ${speed:-Unknown} Mbps"
        echo
    done
}

get_partition_info() {
    echo "System Partitions:"
    partitions=$(df -h --output=source,size,used,avail,target | grep "^/dev/")
    echo """$partitions" | awk '{print "Mount Point:", $5, "Size:", $2, "Used:", $3, "Available:", $4}'
}

main() {
    echo "System Information:"
    get_os_info
    echo ""
    get_cpu_info
    echo ""
    get_memory_info
    echo ""
    get_network_info
    get_partition_info
}

main
