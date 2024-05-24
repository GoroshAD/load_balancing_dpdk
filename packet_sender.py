from scapy.all import sendp, IP, Ether, UDP, rdpcap
import cmd
import time

class sender(cmd.Cmd):
    """packet sender"""
    prompt = ":"

    def do_rnd_send(self, args):
        "send 256 random packets NUM times"
        try:
            sendp(Ether()/IP(dst="170.210.254.4", src="2.2.2.2/24")/UDP(dport=999,sport=666)/f"Hello world!",iface="enp4s0f1", count=int(args))
        except:
            print("wrong args")

    def do_fix_send(self, args):
        "send NUM same packets"
        try:
            sendp(Ether()/IP(dst="172.21.253.4")/UDP(dport=999,sport=666)/f"Hello world!",iface="enp4s0f1", count=int(args))
        except:
            print("wrong args")

    def do_file_send(self, args):
        "send a file with PATH NUM times"
        try:
            file_path, times = args.split()
            times = int(times)
            for i in range(times):
                sendp(rdpcap(file_path),iface="enp4s0f1")
        except:
            print("wrong args")

    def do_testing(self, args):
        "start testing with NUM files in dir PATH"
        try:
            folder_path, exps = args.split()
            exps = int(exps)
            for i in range(1, exps + 1):
                if folder_path[len(folder_path) - 1] != "/":
                    folder_path += "/"
                sendp(rdpcap(folder_path + f"test_{i}.pcap"),iface="enp4s0f1")
        except:
            print("wrong args")

    def do_EOF(self, args):
        return True

if __name__ == "__main__":
    sender().cmdloop()


