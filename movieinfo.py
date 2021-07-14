from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import imdb


def find():

    if MovieSearch.get() == '':
        messagebox.showerror('Error', 'Please Type A Movie Name')
    else:
        root1 = Toplevel()
        root1.geometry('950x600+200+50')
        root1.title('Desi Tech Movie Information')
        root1.config(bg='orange')

        title_label = Label(root1, text='Title', font=('cooper black', 30, 'bold'), fg='white', bg='orange')
        title_label.place(x=60, y=30)

        title_name_label = Label(root1, font=('cooper black', 20, 'bold'), fg='white', bg='orange')
        title_name_label.place(x=300, y=30)

        director_label = Label(root1, text='Director', font=('cooper black', 30, 'bold'), fg='white', bg='orange')
        director_label.place(x=60, y=100)

        director_name_label = Label(root1, font=('cooper black', 20, 'bold'), fg='white', bg='orange')
        director_name_label.place(x=300, y=100)

        year_label = Label(root1, text='Year', font=('cooper black', 30, 'bold'), fg='white', bg='orange')
        year_label.place(x=60, y=170)

        year_name_label = Label(root1, font=('cooper black', 20, 'bold'), fg='white', bg='orange')
        year_name_label.place(x=300, y=170)

        runtime_label = Label(root1, text='Runtime', font=('cooper black', 30, 'bold'), fg='white', bg='orange')
        runtime_label.place(x=60, y=240)

        runtime_name_label = Label(root1, font=('cooper black', 20, 'bold'), fg='white', bg='orange')
        runtime_name_label.place(x=300, y=240)

        genre_label = Label(root1, text='Genre', font=('cooper black', 30, 'bold'), fg='white', bg='orange')
        genre_label.place(x=60, y=310)

        genre_name_label = Label(root1, font=('cooper black', 20, 'bold'), fg='white', bg='orange')
        genre_name_label.place(x=300, y=310)

        rating_label = Label(root1, text='Rating', font=('cooper black', 30, 'bold'), fg='white', bg='orange')
        rating_label.place(x=60, y=380)

        rating_name_label = Label(root1, font=('cooper black', 20, 'bold'), fg='white', bg='orange')
        rating_name_label.place(x=300, y=380)

        cast_label = Label(root1, text='Cast', font=('cooper black', 30, 'bold'), fg='white', bg='orange')
        cast_label.place(x=60, y=450)

        cast_name_label = Label(root1, font=('cooper black', 15, 'bold'), fg='white', bg='orange', wraplength=615
                                , justify=LEFT)
        cast_name_label.place(x=300, y=450)

        imdb_object = imdb.IMDb()
        movie_name = MovieSearch.get()
        movies = imdb_object.search_movie(movie_name)
        index = movies[0].getID()
        movie = imdb_object.get_movie(index)
        title = movie['title']
        title_name_label.config(text=title)

        year = movie['year']
        year_name_label.config(text=year)

        rating = movie['rating']
        rating_name_label.config(text=rating)

        genre = movie['genre']
        genre_name_label.config(text=genre)

        for director in movie['director']:
            director_name_label.config(text=director)

        for runtime in movie['runtime']:
            hours = int(runtime) // 60
            minutes = int(runtime) % 60

            runtime_name_label.config(text=f'{hours} HOURS {minutes} MINUTES')

        cast = movie['cast']
        cast_list = list(map(str, cast))
        my_list = cast_list[:10]
        x = ' '
        for i in my_list:
            if i == my_list[9]:
                x = x + i + '.'
            else:
                x = x + i + ',' + ' '

        cast_name_label.config(text=x)

        root1.mainloop()


root = Tk()

root.geometry('1057x655+100+30')
root.title('Desi Tech')
root.resizable(False,False)
load = Image.open('movie1.jpg')
render = ImageTk.PhotoImage(load)
img = Label(root, image = render)
img.place(x=0, y=0)

MovieLabel = Label(root, text='Movie Name:', font=('algerian', 20, 'bold'), bg='#FFFFFF')
MovieLabel.place(x=250, y=307)

MovieSearch = Entry(root, font=('algerian', 18, 'bold'), bd=10, relief=GROOVE)
MovieSearch.place(x=435, y=310)
MovieSearch.focus_set()

movie_search_button = Button(root, text='SEARCH',font=('algerian', 15, 'bold'),bd=10, relief=GROOVE, command=find)
movie_search_button.place(x=722, y=305)
root.mainloop()