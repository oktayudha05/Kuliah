import pygame
import sys
import random

# Inisialisasi Pygame
pygame.init()

# Konstanta
WIDTH, HEIGHT = 900, 600
FPS = 30
BLACK = (255, 255, 255)
WHITE = (0, 0, 0)
FONT = pygame.font.Font(None, 36)

# Inisialisasi layar
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Gerbang Logika")

# Inisialisasi variabel
score = 0
question_text = ""
correct_gate = ""

# Fungsi untuk menampilkan pertanyaan
def show_question():
    global question_text, correct_gate
    a = random.choice([0, 1])
    b = random.choice([0, 1])

    # Pilih gerbang logika secara acak
    gate_type = random.choice(["AND", "OR"])

    # Hitung jawaban yang benar
    if gate_type == "AND":
        correct_answer = a and b
    else:
        correct_answer = a or b

    # Tampilkan pertanyaan
    question_text = f"What is {a} {gate_type} {b}?"
    correct_gate = gate_type

# Fungsi untuk menampilkan skor
def show_score():
    score_text = FONT.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Fungsi untuk menampilkan teks pertanyaan
def show_question_text():
    question_surface = FONT.render(question_text, True, WHITE)
    screen.blit(question_surface, (WIDTH // 2 - question_surface.get_width() // 2, 200))

# Fungsi untuk menampilkan teks jawaban yang benar
def show_correct_gate():
    correct_gate_surface = FONT.render(f"Correct gate: {correct_gate}", True, WHITE)
    screen.blit(correct_gate_surface, (WIDTH // 2 - correct_gate_surface.get_width() // 2, 250))

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_o:
                # Jawaban benar jika pemain memilih gerbang yang benar sesuai pertanyaan
                if (event.key == pygame.K_a and correct_gate == "AND") or (event.key == pygame.K_o and correct_gate == "OR"):
                    score += 1
                show_question()

    # Tampilkan background
    screen.fill(BLACK)

    # Tampilkan pertanyaan, skor, dan jawaban yang benar
    show_question_text()
    show_score()
    show_correct_gate()

    # Update layar
    pygame.display.flip()

    # Atur kecepatan frame
    clock.tick(FPS)

# Keluar dari aplikasi Pygame
pygame.quit()
sys.exit()
