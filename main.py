import tkinter as tk
import time
import random
import _thread as thr

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("220x140")
        self.root.title("BluMark")

        self.score_label = tk.Label(self.root, text="0", bg="lightblue", font=('Arial', 32, 'bold'))
        self.score_label.pack(pady=10, ipadx=30)
        
        tk.Button(self.root, text="Run", command=self.run).pack(ipady=10, ipadx=70)

    def run(self):
        thr.start_new_thread(self.benchmark, ())

    def benchmark(self, duration=0.5):

        self.score_label.config(text="-")

        scores = [["fpc_score", "fpa_score", "fpm_score", "fpd_score", "brs_score", "brm_score"]]
        scores.append([])

        fpc_single_start = time.time()
        fpc_score = 0
        while time.time() - fpc_single_start < duration:
            fpc_score += 1
        
        scores[1].append(fpc_score)


        fpa_single_start = time.time()
        fpa_score = 0
        fpa_temp = 0.0
        while time.time() - fpa_single_start < duration:
            fpa_temp += random.random()
            fpa_score += 1
        
        scores[1].append(fpa_score)

        fpm_single_start = time.time()
        fpm_score = 0
        fpm_temp = 0.0
        while time.time() - fpm_single_start < duration:
            fpm_temp *= random.random()
            fpm_score += 1
        
        scores[1].append(fpm_score)

        fpd_single_start = time.time()
        fpd_score = 0
        fpd_temp = 0.0
        while time.time() - fpd_single_start < duration:
            fpd_temp /= random.random()
            fpd_score += 1
        
        scores[1].append(fpd_score)

        brs_single_start = time.time()
        brs_score = 0
        brs_temp = 0.0
        while time.time() - brs_single_start < duration:
            if random.random() > 0.5:
                brs_temp += 1
            else:
                brs_temp -= 1

            brs_score += 1
        
        scores[1].append(brs_score)

        brm_single_start = time.time()
        brm_score = 0
        brm_temp = 0.0
        while time.time() - brm_single_start < duration:
            brm_temp = random.random()

            if brm_temp > 0.75:
                brm_temp += 1
            elif brm_temp > 0.5:
                brm_temp -= 1
            elif brm_temp > 0.25:
                brm_temp += 1
            else:
                brm_temp -= 1

            brm_score += 1
        
        scores[1].append(brm_score)

        for score in scores:
            for element in score:
                print(f"{element:<20}", end="")
            print("")

        print(f"\nScore:{sum(scores[1])/1000}")
        self.score_label.config(text=f"{int(sum(scores[1])/1000)}")
        



app = App()
app.root.mainloop()