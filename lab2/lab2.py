from datetime import date


class Aluno:
    def __init__(self, nome, DRE, matricula = "ativa"):
        """Cria um objeto da classe Aluno com atributos nome, DRE, matricula"""
        self.nome = nome
        self.DRE = DRE
        self.matricula = matricula

    def alterarMatricula(self, matricula):
        """Altera a matricula"""
        if self.matricula == matricula:
            print("A matrícula já está " + matricula)
        else:
            self.matricula = matricula
            print("A matrícula foi alterada para " + matricula)

    def dados(self):
        """Retorna uma descrição de um objeto da classe"""
        return "{}\t{}\tmatricula {}".format(self.nome, str(self.DRE), self.matricula)

    def __str__(self):
        """Retorna uma descrição de um objeto da classe"""
        return "{}\t{}\tmatricula {}".format(self.nome, str(self.DRE), self.matricula)


class Disciplina:
    """Classe representa o conceito de uma disciplina na UFRJ"""
    def __init__(self, nome, vagas = 0):
        """Cria um objeto da classe com atributos nome, vagas, alunos"""
        self.nome = nome
        self.vagas = vagas
        self.alunos = [] # self.alunos é um atributo global criado automaticamente

    def __add__(self, other):
        """Junta duas disciplinas se o nome delas for idêntico"""
        if self.nome == other.nome:
            return Disciplina(self.nome, self.vagas + other.vagas)
        else:
            print("Não foi possível juntar as turmas")

    def inscreverAluno(self, aluno):
        """Inscreve um objeto da classe Aluno na disciplina se tiver
        vagas livres ou o Aluno não for ainda inscrito na disciplina"""
        if len(self.alunos) < self.vagas and aluno not in self.alunos:
            self.alunos.append(aluno)
        elif aluno in self.alunos:
            print("aluno {} já está inscrito na disciplina".format(aluno.nome))
        else:
            print("Vagas esgotadas")

    def consultarVagas(self):
        """Retorna uma string que diz o número de vagas totais e vagas
        livres na disciplina"""
        return  'Vagas totais: {0}. Vagas livres: {1}'.format(self.vagas, self.vagas - len(self.alunos))

    def __str__(self):
        """Retorna uma descrição de um objeto da classe"""
        # mostra a quantidade de vagas totais e restantes
        # se tiver alunos inscritos, também mostra seus nomes, DRE e matrícula
        if len(self.alunos) == 0:
          return self.nome + ', sem alunos inscritos.' + '\n' +  \
          self.consultarVagas()

        elif len(self.alunos) < self.vagas:
          return 'Computação II, alunos inscritos:' + '\n' + \
          '\n'.join([str(inscrito) for inscrito in self.alunos]) + '\n' + \
          self.consultarVagas()

        else:
          return 'erro'


class Pessoa:
    def __init__(self, nome, dataNascimento, nomeDeMae, nomeDePai):
      """Cria um objeto da classe Pessoa com atributos nome, dataNascimento, nomeDeMae e nomeDePai"""
      self.nome = nome
      self.dataNascimento = dataNascimento
      self. nomeDeMae = nomeDeMae
      self.nomeDePai = nomeDePai

    def idade(self, data=date.today().strftime("%d/%m/%Y")):
      """Retorna um inteiro que é a idade da pessoa na data que o programa for rodado"""
      # faz primeiro a comparação dos anos, depois dos meses e dias
      # subtrai 1 se não passar no teste do mês e dia
      dataNascimento = self.dataNascimento
      return int(data[-4:]) - int(dataNascimento[-4:]) - \
      ((int(data[3:5]), int(data[:2])) < (int(dataNascimento[3:5]), int(dataNascimento[:2])))

    def __str__(self):
      """Retorna uma descrição de um objeto da classe"""
      return 'nome: {}, idade: {}, mae: {}, pai: {}'.format(self.nome, self.idade(), self.nomeDeMae, self.nomeDePai)
