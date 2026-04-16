tarefas = []
print("Vamos começar nossa lista de tarefas de hoje:")
quantidade = int(input("Quantas tarefas temos hoje? "))
for i in range(quantidade):
	lista = input(f"Digite a {i+1}° tarefa: ").strip().lower()
	tarefas.append(lista)
while len(tarefas) > 0:
	print ("\n-------------------------------------------------")
	if len(tarefas) == quantidade:
		print ("Sua lista de hoje é: ")
	else:
		print(f"Sua lista atualizada ficou: {len(tarefas)} restantes")
	for lista in tarefas:
		print(f"-{lista}")
	print ("\n-------------------------------------------------")
	concluida = input("\nQual tarefa você ja terminou?").strip().lower()
	if concluida in tarefas:
		tarefas.remove(concluida)
		print (f"\nOba! {concluida} foi concluida com sucesso e já foi removida da lista")
		restante = len(tarefas)
		print(f"\nAinda restam {restante} tarefas na sua lista")
	else:
		print(" Ops essa tarefa não está na lista! Digite exatamente como aparece")
print("\n" + "="*30)
print("🚀 PARABÉNS, RODRIGO! \nTodas as tarefas foram concluídas. \nTurno finalizado com sucesso!")
print("="*30)