from sys import argv as args
import distro as ds
import os
import platform
import getpass as gp
import datetime as dt
import psutil
if "--clmode" not in args:
    import tkinter as tk
    import webbrowser
# Adicionando um valor placeholder a lista args para caso nn seja passado nenhum argumento
if len(args) == 1:
    args.append('--noargs')


def github():
    # Abrir o repositório do projeto no github pelo nevegador padrão
    webbrowser.open("https://github.com/BrenoMartinsDeOliveiraVasconcelos/linver")


def main():
    if platform.system() == "Windows":
        print("You shouldn't run this on Windows, but anyways")
    linux = ds.name() #ds.linux_distribution()[0]
    if args[1] == '--noargs':
        linux = ds.name() #ds.linux_distribution()[0]
    elif '--distro' in args:
        try:
            linux = args[args.index('--distro') + 1].replace('_', ' ').replace('-', '/')
        except IndexError:
            linux = ds.name() #ds.linux_distribution()[0]
        #linux = args[].replace('_', ' ').replace("-", "/")
    distrover = ds.version() #ds.linux_distribution()[1]
    codename = ds.codename() #ds.linux_distribution()[2]
    build = ds.build_number()
    if build == '0' or build == '':
        build = 'none'
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
        if 'loop' in device.split("/")[-1]:
            pass
        else:
            disks_list.append(device)
    disks_list = sorted(disks_list)
    partitions = len(disks_list)
    discos = {"sda"}
    for disk in disks_list:
        disco = disk.split("/")[-1]
        for i in "1234567890":
            disco = disco.replace(i, "")
        discos.add(disco)

    # Número de discos
    ndiscos = len(discos)
    
    # Conseguir o uptime
    uptime = dt.datetime.now() - dt.datetime.fromtimestamp(psutil.boot_time())
    uptime = (str(uptime).split('.')[0]).split(":")
    for i in range(len(uptime)):
        uptime[i] = int(uptime[i])

    uptimestr = f"{uptime[0]} hour{'s' if uptime[0] > 1 else ''}, {uptime[1]} minute{'s' if uptime[1] > 1 else ''} and {uptime[2]} second{'s' if uptime[2] > 1 else ''}."

    script_path = os.path.dirname(os.path.realpath(__file__))

    linver = f"""{linux} 
Version {distrover} {codename} (Build {build}, kernel {kernelver})
© {year}.

Linver is a free and open source product.

This machine is using {memused}GB of its {memtotal}GB RAM.
There are {partitions} partitions mounted across {ndiscos} disk{'s' if ndiscos > 1 else ""}.
({', '.join(disks_list)}.)

Host name: {platform.node()}
Uptime: {uptimestr}

Thank your for using this program, {gp.getuser()}! ^-^
    """
    if '--clmode' not in args:
        # Váriabel image como linux.png como placeholder
        image = f"{script_path}/assets/linux.png"

        # Aqui muda a imagem de acordo com a distro
        try:
            open(f"{script_path}/assets/{linux.replace(' ', '_').replace('/', '-')}.png", 'r')
            image = f"{script_path}/assets/{linux.replace(' ', '_').replace('/', '-')}.png"
        except FileNotFoundError:
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

    # # Criar uma divisória abaixo da imagem
    # div = tk.Frame(root, bg="#828282", width=510, height=1)
    # emptydiv = tk.Frame(root, bg="#ffffff", width=20, height=1)
    # emptydiv2 = tk.Frame(root, bg="#ffffff", width=20, height=1)
    # emptydiv.grid(row=2, column=0, columnspan=1, rowspan=2, sticky="nsew")
    # div.grid(row=2, column=1, columnspan=3, rowspan=2, sticky="nsew")
    # emptydiv2.grid(row=2, column=4, columnspan=1, rowspan=2, sticky="nsew")

        # Criar label com o texto
        label = tk.Label(root, text=linver, bg="#ffffff", fg=fontcolor)
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
    else:
        print(linver)

if __name__ == '__main__':
    main()
