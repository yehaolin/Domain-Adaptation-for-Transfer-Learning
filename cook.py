import tkinter
import tkinter.messagebox
import test_modle

def select_func_TCA(frame, win):
    global name
    name = 'TCA'
    frame.destroy()
    second_menu(win)


def select_func_JDA(frame, win):
    global name
    name = 'JDA'
    frame.destroy()
    second_menu(win)


def select_func_BDA(frame, win):
    global name
    name = 'BDA'
    frame.destroy()
    second_menu(win)


def main_menu(win):
    global frame
    frame = tkinter.Frame(win, bg='palegoldenrod', width=900, height=600)
    frame.place(x=0, y=0)

    label1_1 = tkinter.Label(frame, bg='palegoldenrod', text='The CNN with transfer learning', font=('Arial', 30))
    label1_1.place(x=150 + 50, y=50)

    button1 = tkinter.Button(frame, text='TCA', font=('Arial', 20), bg='darkgoldenrod',
                             command=lambda: select_func_TCA(frame, win))
    button1.place(x=100, y=300-100)

    button2 = tkinter.Button(frame, text='JDA', font=('Arial', 20), bg='darkgoldenrod',
                             command=lambda: select_func_JDA(frame, win))
    button2.place(x=400, y=300-100)

    button3 = tkinter.Button(frame, text='BDA', font=('Arial', 20), bg='darkgoldenrod',
                             command=lambda: select_func_BDA(frame, win))
    button3.place(x=700, y=300-100)
    button3 = tkinter.Button(frame, text='Auto calculate all', font=('Arial', 20), bg='darkgoldenrod',
                             command=lambda: auto_compute(win))
    button3.place(x=320, y=400)


def third_menu(win):
    global data_source
    global data_target
    global name
    if data_target == data_source:
        tkinter.messagebox.showerror(title='fatal error', message='都说了俩个域不能一样')
        return
    else:
        tkinter.messagebox.showinfo(title='success', message='导入成功')
    win2 = tkinter.Toplevel(win)
    win2.title('ACC'+name)
    win2.geometry('500x200')
    frame = tkinter.Frame(win2, bg='moccasin', width=500, height=100)
    frame.place(x=0, y=0)
    label2_1 = tkinter.Label(win2, bg='moccasin', font=('Arial', 20),
                             text=('The acc of '+data_target+data_source+' dataset by '+name))
    label2_1.place(x=50, y=50)
    frame1 = tkinter.Frame(win2, bg='goldenrod', width=500, height=100)
    frame1.place(x=0, y=100)
    filename = 'img/'+name+data_source+data_target+'/target'
    weight = 'weights/'+name+data_source+data_target+'.pth'
    acc = test_modle.cnn_compute(filename, weight)
    label2_4 = tkinter.Label(win2, bg='goldenrod', font=('Arial', 15), width=30)
    label2_4.place(x=75, y=150)
    label2_4.config(text='Accuracy : ' + str(acc))  # display the accuracy


def second_menu(win):
    var_kernel = tkinter.StringVar()
    var_kernel.set('1')
    var_kernel_2 = tkinter.StringVar()
    var_kernel_2.set('3')
    global data_source
    data_source = var_kernel.get()
    global data_target
    data_target = var_kernel_2.get()

    canvas = tkinter.Canvas(win, bg='palegoldenrod', height=600, width=900)
    canvas.place(x=0, y=0)
    button1_1 = tkinter.Button(canvas, text='Back', font=('Arial', 15), bg='darkgoldenrod',
                               command=lambda: main_menu(win))
    button1_1.place(x=50, y=20)
    button1_1 = tkinter.Button(canvas, text='Next', font=('Arial', 15), bg='darkgoldenrod',
                               command=lambda: third_menu(win))
    button1_1.place(x=800, y=20)
    label2_1 = tkinter.Label(canvas, bg='palegoldenrod', text='Source', font=('Arial', 30))
    label2_1.place(x=100, y=100)
    label2_2 = tkinter.Label(canvas, bg='palegoldenrod', text='Target', font=('Arial', 30))
    label2_2.place(x=650, y=100)

    def line_create(data_source, data_target):
        global line
        canvas.delete(line)
        num_xs = int(data_source)
        num_xt = int(data_target)

        if num_xt == num_xs:
            line = canvas.create_line(270, (num_xs + 1) * 100 + 20, 605, (num_xt + 1) * 100 + 20, width=10,
                                      fill='red')
            tkinter.messagebox.showerror(title='error', message='源域与目标域不能相等')
        else:
            line = canvas.create_line(270, (num_xs + 1) * 100 + 20, 605, (num_xt + 1) * 100 + 20, width=10,
                                      fill='skyblue')

    def select_source(var):
        global line
        global data_source
        global data_target
        data_source = var.get()
        line_create(data_source, data_target)

    def select_target(var):
        global data_target
        data_target = var.get()
        global data_source
        global line
        line_create(data_source, data_target)

    def display_choose(x=50, func=select_source, var=var_kernel):
        radiobutton1 = tkinter.Radiobutton(canvas, text='caltech  ', variable=var, value='1', font=('Arial', 20),
                                           bg='darkgoldenrod', command=lambda: func(var), width=12)

        radiobutton2 = tkinter.Radiobutton(canvas, text='amazon ', variable=var, value='2', font=('Arial', 20),
                                           bg='darkgoldenrod', command=lambda: func(var), width=12)

        radiobutton3 = tkinter.Radiobutton(canvas, text='webcam', variable=var, value='3', font=('Arial', 20),
                                           bg='darkgoldenrod', command=lambda: func(var), width=12)

        radiobutton4 = tkinter.Radiobutton(canvas, text='dslr        ', variable=var, value='4', font=('Arial', 20),
                                           bg='darkgoldenrod', command=lambda: func(var), width=12)
        radiobutton1.place(x=x, y=200)
        radiobutton2.place(x=x, y=300)
        radiobutton3.place(x=x, y=400)
        radiobutton4.place(x=x, y=500)

    display_choose(x=50)
    display_choose(x=600, func=select_target, var=var_kernel_2)
    global line
    line = canvas.create_line(270, 220, 605, 420, width=10, fill='skyblue')

def auto_compute(win):
    algorithm = ['TCA', 'JDA', 'BDA']
    win2 = tkinter.Toplevel(win)
    win2.title('acc')
    win2.geometry('1200x500')
    frame1 = tkinter.Frame(win2, bg='goldenrod', width=1200, height=500)
    frame1.place(x=0, y=0)
    label_1 = tkinter.Label(frame1, bg='goldenrod', font=('Arial', 25), text='')
    label_1.config(text='所有数据集测试结果')
    label_1.place(x=450, y=10)
    for i in range(3):
        length_x = 0
        label = tkinter.Label(win2, bg='goldenrod', font=('Arial', 20), text=(algorithm[i]))
        label.place(y=50+(i+1)*100, x=20)
        length = 0
        for j in range(4):
            for k in range(4):
                if j != k:
                    length += 1
                    label = tkinter.Label(win2, bg='goldenrod', font=('Arial', 15), text=(str(j+1)+' '+str(k+1)))
                    label.place(x=60+length*80, y=100)
                    length_x += 1
                    filename = 'img/' + algorithm[i] + str(j + 1) + str(k + 1) + '/target'
                    weight = 'weights/'+ algorithm[i] + str(j + 1) + str(k + 1)+'.pth'
                    acc = test_modle.cnn_compute(filename, weight)
                    label = tkinter.Label(win2, bg='goldenrod', font=('Arial', 15), text='')
                    label.place(x=60 + length_x * 80, y=50 + (i + 1) * 100)
                    acc = float('%.4f' % acc)
                    label.config(text=str(acc))
                    print(length_x)


if __name__ == '__main__':
    line = None
    data_source = None
    data_target = None
    name = None
    win = tkinter.Tk()
    win.title('little sheep')
    win.geometry('900x700')
    main_menu(win)
    win.mainloop()
