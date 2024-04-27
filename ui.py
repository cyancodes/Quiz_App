from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):  # Called when a new object created
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        # Score label
        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 10, "normal"))
        self.score_label.grid(column=1, row=0)

        #  Canvas
        self.canvas = Canvas(
            width=300,
            height=250,
            bg="white",
            highlightthickness=0
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=40)

        #  Quiz Text
        self.canvas_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Quiz Text",
            font=("Arial", 15, "italic"),
            fill=THEME_COLOR
        )

        #  Buttons
        self.true_button = self.button_maker(
            image="images/true.png",
            button_action=self.true,
            button_column=0
        )

        self.false_button = self.button_maker(
            image="images/false.png",
            button_action=self.false,
            button_column=1
        )

        self.get_next_question()
        self.window.mainloop()

    def button_maker(self, image, button_action, button_column):
        button_image = PhotoImage(file=image)
        button = Button(self.window, image=button_image, command=button_action, highlightthickness=0, bg=THEME_COLOR)
        button.image = button_image
        button.grid(column=button_column, row=2)
        return button

    def button_actions(self, boolean):
        if self.quiz.check_answer(boolean):  # triggers this statement if answered correctly
            self.give_feedback(colour="green")
        else:
            self.give_feedback(colour="red")

        self.window.after(500, self.get_next_question)

        # if self.quiz.still_has_questions():
        #     self.get_next_question()

    def true(self):
        self.button_actions(boolean="true")

    def false(self):
        self.button_actions(boolean="false")

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")  # Update score
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=question)
        else:
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.itemconfig(
                self.canvas_text,
                text=f"You've finished the quiz!\n"
                     f"Your final score was {self.quiz.score}"
            )

    def give_feedback(self, colour):
        self.canvas.config(bg=colour)
        self.canvas.update()
