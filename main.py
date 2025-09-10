# n = Quantidade de alunos
# t = Número de times a serem formados
n, t = map(int, input().split())

alunos = []
for _ in range(n):
    nome, habilidade = input().split()
    alunos.append([nome, int(habilidade)])

alunos.sort(key=lambda x: x[1])
times = [[] for _ in range(t)]

while True:
    for time in times:
        if alunos:
            time.append(alunos.pop()[0])
    
    if not alunos:
        break

for index, time in enumerate(times, start=1):
    time.sort()

    print(f"Time {index}")
    for aluno in time:
        print(f"{aluno}")
    print("")
