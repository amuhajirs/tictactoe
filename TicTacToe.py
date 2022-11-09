import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Tic-Tac-Toe')
        self.photo = tk.PhotoImage(file='C:/Users/HP/Pictures/foto/J item.png')
        self.iconphoto(False, self.photo)
        self._frame = None
        self.switch_frame(TicTacToeMenu)

    def switch_frame(self, frame_class):
        # Destroys current frame and replaces it with a new one
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class TicTacToeMenu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text='Tic-Tac-Toe', font=('Arial', 30), fg='white', bg='black').pack()
        tk.Button(self, text='Start', font=('Arial', 15), width=18, fg='white', bg='#373737', command=lambda: master.switch_frame(TicTacToeBoard)).pack()
        tk.Button(self, text='Exit', font=('Arial', 15), width=18, fg='white', bg='#373737', command=lambda: exit()).pack()

        master.bind('<Return>', lambda event: master.switch_frame(TicTacToeBoard))
        master.bind('<Escape>', lambda event: exit())

class TicTacToeBoard(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg='black')
        self.players = ['x', 'o']
        self.current_turn = self.players[0]
        self.turn_label = tk.Label(self, text=f'{self.current_turn} turn', font=('Arial', 30), bg='black', fg='white')
        self.turn_label.pack(side='top')
        self.board = [
            ['--', '--', '--'],
            ['--', '--', '--'],
            ['--', '--', '--']
        ]

        frame = tk.Frame(self)
        frame.pack()

        for row in range(3):
            for column in range(3):
                self.board[row][column] = tk.Button(frame, text='', font=('arial', 20), width=5, height=2, fg='white', bg='#373737', command=lambda row=row, column=column: self.next_turn(row, column))
                self.board[row][column].grid(row=row, column=column)

        tk.Button(self, text='Restart', font=('Arial', 15), width=8, bg='#373737', fg='white', command=lambda: self.new_game()).pack()
        tk.Button(self, text='Exit', font=('Arial', 15), width=8, bg='#373737', fg='white', command=lambda: exit()).pack(side='bottom')
        master.bind('<Return>', lambda event: self.new_game())
        master.bind('1', lambda event: self.next_turn(0,0))
        master.bind('2', lambda event: self.next_turn(0,1))
        master.bind('3', lambda event: self.next_turn(0,2))
        master.bind('4', lambda event: self.next_turn(1,0))
        master.bind('5', lambda event: self.next_turn(1,1))
        master.bind('6', lambda event: self.next_turn(1,2))
        master.bind('7', lambda event: self.next_turn(2,0))
        master.bind('8', lambda event: self.next_turn(2,1))
        master.bind('9', lambda event: self.next_turn(2,2))

    def next_turn(self, row, column):
        if self.board[row][column]['text'] == '' and self.check_winner() is False:
            self.board[row][column]['text'] = self.current_turn
            if self.check_winner() is False:
                if self.current_turn == self.players[0]:
                    self.current_turn = self.players[1]
                    self.turn_label['text'] = f'{self.current_turn} turn'
                else:
                    self.current_turn = self.players[0]
                    self.turn_label['text'] = f'{self.current_turn} turn'

            elif self.check_winner() is True:
                self.turn_label['text'] = f'{self.current_turn} win!'

            elif self.check_winner() == 'Tie':
                self.turn_label['text'] = 'Tie'

    def check_winner(self):
        # Check Row
        for row in range(3):
            if self.board[row][0]['text'] == self.board[row][1]['text'] == self.board[row][2]['text'] != '':
                # Change button's background color when someone win
                self.board[row][0]['bg']= 'green'
                self.board[row][1]['bg']= 'green'
                self.board[row][2]['bg']= 'green'
                return True

        # Check Column
        for column in range(3):
            if self.board[0][column]['text'] == self.board[1][column]['text'] == self.board[2][column]['text'] != '':
                # Change button's background color when someone win
                self.board[0][column]['bg']= 'green'
                self.board[1][column]['bg']= 'green'
                self.board[2][column]['bg']= 'green'
                return True

        # Check Diagonal
        if self.board[0][0]['text'] == self.board[1][1]['text'] == self.board[2][2]['text'] != '':
            # Change button's background color when someone win
            self.board[0][0]['bg']= 'green'
            self.board[1][1]['bg']= 'green'
            self.board[2][2]['bg']= 'green'
            return True

        elif self.board[0][2]['text'] == self.board[1][1]['text'] == self.board[2][0]['text'] != '':
            # Change button's background color when someone win
            self.board[0][2]['bg']= 'green'
            self.board[1][1]['bg']= 'green'
            self.board[2][0]['bg']= 'green'
            return True

        # Check Tie
        else:
            self.spaces = 9
            for row in range(3):
                for column in range(3):
                    if self.board[row][column]['text'] != '':
                        self.spaces -= 1
            if self.spaces == 0:
                return 'Tie'

        # Game isn't over
        return False

    def new_game(self):
        for row in range(3):
            for column in range(3):
                self.board[row][column]['text'] = ''
                self.board[row][column]['bg'] ='#373737'
        self.current_turn = self.players[0]
        self.turn_label['text'] = f'{self.current_turn} turn'

if __name__ == '__main__':
    tictactoe = App()
    tictactoe.mainloop()