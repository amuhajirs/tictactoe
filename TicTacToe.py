# Import required library
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        # Create window
        tk.Tk.__init__(self)
        self.title('Tic-Tac-Toe')
        self.configure(bg='black')
        self.iconbitmap('ttt_icon.ico')
        self.frame = None
        
        # Go to main menu of TicTacToe
        self.switch_frame(TicTacToeMenu)
        
    def switch_frame(self, frame_class):
        # Function for switch frame by destroy current frame and replaces it with a new one
        new_frame = frame_class(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = new_frame
        self.frame.pack(expand=True)

class TicTacToeMenu(tk.Frame):
    def __init__(self, master):
        # Main menu of TicTacToe
        tk.Frame.__init__(self, master)
        self.configure(bg='black')
        tk.Label(self, text='Tic-Tac-Toe', font=('Arial', 30), fg='white', bg='black').pack(pady=20, padx=20)
        tk.Button(self, text='Start', font=('Arial', 15), width=18, fg='white', bg='#373737', command=lambda: master.switch_frame(TicTacToeGame)).pack(pady=2)
        tk.Button(self, text='Exit', font=('Arial', 15), width=18, fg='white', bg='#373737', command=lambda: master.destroy()).pack(pady=(2, 20))

        # Shortcut key for go to TicTacToe game and exit 
        master.bind('<Return>', lambda event: master.switch_frame(TicTacToeGame))
        master.bind('<Escape>', lambda event: master.destroy())

class TicTacToeGame(tk.Frame):
    def __init__(self, master):
        # TicTacToe game
        tk.Frame.__init__(self, master)
        self.configure(bg='black')
        self.players = [['X', 'red'], ['O', 'blue']]
        self.current_turn = self.players[0]

        self.turn_label = tk.Label(self, text=f'{self.current_turn[0]} turn', font=('Arial', 30), bg='black', fg=self.current_turn[1])
        self.turn_label.pack(side='top', pady=20)
        self.board = [
            ['--', '--', '--'],
            ['--', '--', '--'],
            ['--', '--', '--']
        ]

        # Make boxes by using buttons to play tictactoe
        self.box_frame = tk.Frame(self)
        self.box_frame.pack()
        for row in range(3):
            for column in range(3):
                self.board[row][column] = tk.Button(self.box_frame, text='', font=('arial', 20), width=5, height=2, fg='white', bg='#373737', command=lambda row=row, column=column: self.next_turn(row, column))
                self.board[row][column].grid(row=row, column=column)

        # Restart and exit button
        self.button_frame = tk.Frame(self)
        self.button_frame.configure(bg='black')
        self.button_frame.pack(padx=20, pady=20)
        tk.Button(self.button_frame, text='Restart', font=('Arial', 15), width=8, bg='#373737', fg='white', command=lambda: self.new_game()).grid(row=0, column=0, padx=2)
        tk.Button(self.button_frame, text='Back', font=('Arial', 15), width=8, bg='#373737', fg='white', command=lambda: master.switch_frame(TicTacToeMenu)).grid(row=0, column=1, padx=2)
        tk.Button(self.button_frame, text='Exit', font=('Arial', 15), width=8, bg='#373737', fg='white', command=lambda: master.destroy()).grid(row=0, column=2, padx=2)

        # Shortkut Key
        master.bind('<Return>', lambda event: self.new_game())
        master.bind('<BackSpace>', lambda event: master.switch_frame(TicTacToeMenu))
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
        # If the button is pressed, it will chenge text button to 'X' or 'O'
        if self.board[row][column]['text'] == '' and self.check_winner() is False:
            self.board[row][column]['text'] = self.current_turn[0]
            self.board[row][column]['fg'] = self.current_turn[1]
            
            # Changed the label for who is running now
            if self.check_winner() is False:
                if self.current_turn == self.players[0]:
                    self.current_turn = self.players[1]
                    self.turn_label['text'] = f'{self.current_turn[0]} turn'
                    self.turn_label['fg'] = self.current_turn[1]
                else:
                    self.current_turn = self.players[0]
                    self.turn_label['text'] = f'{self.current_turn[0]} turn'
                    self.turn_label['fg'] = self.current_turn[1]

            # Changed the label for who won or drew
            elif self.check_winner() is True:
                self.turn_label['text'] = f'{self.current_turn[0]} win!'
                self.turn_label['fg'] = self.current_turn[1]

            elif self.check_winner() == 'Tie':
                self.turn_label['text'] = 'Tie'
                self.turn_label['fg'] = 'White'

    def check_winner(self):
        # Check row
        for row in range(3):
            if self.board[row][0]['text'] == self.board[row][1]['text'] == self.board[row][2]['text'] != '':
                # Change the background of the button to Green if there is a win
                self.board[row][0]['bg']= 'green'
                self.board[row][1]['bg']= 'green'
                self.board[row][2]['bg']= 'green'
                return True

        # Check column
        for column in range(3):
            if self.board[0][column]['text'] == self.board[1][column]['text'] == self.board[2][column]['text'] != '':
                # Change the background of the button to Green if there is a win
                self.board[0][column]['bg']= 'green'
                self.board[1][column]['bg']= 'green'
                self.board[2][column]['bg']= 'green'
                return True

        # Check Diagonal
        if self.board[0][0]['text'] == self.board[1][1]['text'] == self.board[2][2]['text'] != '':
            # Change the background of the button to Green if there is a win
            self.board[0][0]['bg']= 'green'
            self.board[1][1]['bg']= 'green'
            self.board[2][2]['bg']= 'green'
            return True

        elif self.board[0][2]['text'] == self.board[1][1]['text'] == self.board[2][0]['text'] != '':
            # Change the background of the button to Green if there is a win
            self.board[0][2]['bg']= 'green'
            self.board[1][1]['bg']= 'green'
            self.board[2][0]['bg']= 'green'
            return True

        # Check tie
        else:
            self.spaces = 9
            for row in range(3):
                for column in range(3):
                    if self.board[row][column]['text'] != '':
                        self.spaces -= 1
            if self.spaces == 0:
                return 'Tie'

        # game hasn't finished yet
        return False

    def new_game(self):
        # Function for restart game
        for row in range(3):
            for column in range(3):
                self.board[row][column]['text'] = ''
                self.board[row][column]['bg'] ='#373737'
        self.current_turn = self.players[0]
        self.turn_label['text'] = f'{self.current_turn[0]} turn'
        self.turn_label['fg'] = self.current_turn[1]

if __name__ == '__main__':
    # Start the program
    tictactoe = App()
    tictactoe.mainloop()