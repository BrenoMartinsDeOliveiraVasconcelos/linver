import tkinter as tk
import distro as ds
import os
import platform
import getpass as gp
import datetime as dt
import psutil
import webbrowser


def github():
    # Abrir o repositório do projeto no github pelo nevegador padrão
    webbrowser.open("https://github.com/BrenoMartinsDeOliveiraVasconcelos/linver")


def main():
    linux = ds.linux_distribution()[0]
    distrover = ds.linux_distribution()[1]
    year = dt.date.today().year
    kernelver = platform.release()
    fontcolor = '#141414'
    # Memória RAM
    mem = psutil.virtual_memory()
    memtotal = round(mem.total / (1024 ** 3), 2)
    memused = round(mem.used / (1024 ** 3), 2)
    # Nome ou arquitetura do cpu
    cpu = platform.processor()
    if cpu == '':
        cpu = 'unknown'
    # Discos
    disks = psutil.disk_partitions()
    disks_list = []
    for disk in disks:
        device = disk.device
        if device.split("/")[-1][0:-1] == 'loop':
            pass
        else:
            disks_list.append(device)
    partitions = len(disks_list)
    discos = {"sda"}
    for disk in disks_list:
        discos.add(disk.split("/")[-1][0:-1])

    # Número de discos
    ndiscos = len(discos)
    
    # Conseguir o uptime
    uptime = dt.datetime.now() - dt.datetime.fromtimestamp(psutil.boot_time())
    uptime = (str(uptime).split('.')[0]).split(":")

    uptimestr = f"{uptime[0]} hours, {uptime[1]} minutes and {uptime[2]} seconds."

    script_path = os.path.dirname(os.path.realpath(__file__))

    # Váriabel image como linux.png como placeholder
    image = f"{script_path}/assets/linux.png"

    # Váriabel root como tkinter.Tk()
    root = tk.Tk()
    root.title("Linver")
    #root.geometry("550x470")
    root.resizable(False, False)
    # set background for #ffffff
    root.configure(background="#ffffff")
    
    # Adiciona imagem a janela
    img = tk.PhotoImage(file=image)
    imglabel = tk.Label(root, image=img, bg="#ffffff")
    imglabel.grid(row=0, column=0, columnspan=4, rowspan=2, sticky="nsew")

    # Criar uma divisória abaixo da imagem
    div = tk.Frame(root, bg="#828282", width=510, height=1)
    emptydiv = tk.Frame(root, bg="#ffffff", width=20, height=1)
    emptydiv2 = tk.Frame(root, bg="#ffffff", width=20, height=1)
    emptydiv.grid(row=2, column=0, columnspan=1, rowspan=2, sticky="nsew")
    div.grid(row=2, column=1, columnspan=3, rowspan=2, sticky="nsew")
    emptydiv2.grid(row=2, column=4, columnspan=1, rowspan=2, sticky="nsew")

    # Criar label com o texto
    label = tk.Label(root, text=f"""{linux} 
Version {distrover} (Kernel {kernelver})
© {year}.

This program is a free and open source product.

This product is running on a {memtotal} GB of RAM machine, which  {memused} GB is being used.
The number of partitions mounted is {partitions} in {ndiscos} disk(s).
({', '.join(disks_list)}.)

Machine name is {platform.node()} and its uptime is:
{uptimestr}

{gp.getuser()}

""", bg="#ffffff", fg=fontcolor)
    label.grid(row=4, column=2)


    # Criar botão de sair
    exitbutton = tk.Button(root, text="Ok", bg="#ffffff", fg=fontcolor, 
    command=exit, activebackground="#e0e0e0", borderwidth=1, highlightthickness=0, activeforeground="#000000")
    exitbutton.grid(row=5, column=2, columnspan=1, sticky="nsew")

    # Criar um botão que redireciona para a página do github (https://github.com/BrenoMartinsDeOliveiraVasconcelos/linver)
    githubbutton = tk.Button(root, text="Github", bg="#ffffff", fg=fontcolor, 
    command=github, activebackground="#e0e0e0", borderwidth=1, highlightthickness=0, activeforeground="#000000")
    githubbutton.grid(row=6, column=2, columnspan=1, sticky="nsew")

    root.mainloop()


if __name__ == '__main__':
    main()
