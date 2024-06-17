import tkinter as tk
from tkinter import messagebox

quiz = [
    {
        "question": "What is the capital of France?",
        "choices": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "choices": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "choices": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "answer": "A"
    },
    {
        "question": "What is the square root of 64?",
        "choices": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C"
    }
]


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")

        self.question_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", wraplength=400, justify="left")
        self.question_label.pack(pady=20)

        self.radio_var = tk.StringVar()
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.radio_var, value=chr(65 + i), tristatevalue="x")
            rb.pack(anchor="w")
            self.radio_buttons.append(rb)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)

        self.next_button = tk.Button(root, text="Next", command=self.next_question, state="disabled")
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        question = quiz[self.question_index]
        self.question_label.config(text=question["question"])
        for i, choice in enumerate(question["choices"]):
            self.radio_buttons[i].config(text=choice)
        self.radio_var.set(None)

    def check_answer(self):
        selected_answer = self.radio_var.get()
        if selected_answer:
            question = quiz[self.question_index]
            if selected_answer == question["answer"]:
                self.score += 1
                messagebox.showinfo("Result", "Correct!")
            else:
                messagebox.showinfo("Result", f"Wrong! The correct answer is {question['answer']}.")
            self.submit_button.config(state="disabled")
            self.next_button.config(state="normal")
        else:
            messagebox.showwarning("No answer", "Please select an answer before submitting.")

    def next_question(self):
        self.question_index += 1
        if self.question_index < len(quiz):
            self.load_question()
            self.submit_button.config(state="normal")
            self.next_button.config(state="disabled")
        else:
            messagebox.showinfo("Quiz Finished", f"Your score: {self.score}/{len(quiz)}")
            self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
