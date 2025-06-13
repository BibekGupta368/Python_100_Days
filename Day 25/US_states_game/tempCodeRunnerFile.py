#Getting the coordinates of each and every section 
def get_mouse_click_coor(x, y):
    print(x,y)
timmy.onscreenclick(get_mouse_click_coor)  #When the mouse clicks on the screen ,it will calls the function and passes the x and y coordinates of that clicked section
timmy.mainloop()   #Keeps the screen open

