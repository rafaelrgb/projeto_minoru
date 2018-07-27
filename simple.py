import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#list of tuples for each pacient
pacients_list = [( 1, "Gabriel Leandro Luan Vieira", "1966-08-22", "m", "" ),
                 ( 2, "César Miguel Thiago Gonçalves", "1971-12-20", "m", "" ),
                 ( 3, "Pedro Henrique Erick Pereira", "1979-12-15", "m", "" ),
                 ( 4, "Francisca Sabrina Camila Nogueira", "1968-10-24", "f", "" ),
                 ( 5, "César Victor Yuri Fernandes", "1963-09-21", "m", "" ),
                 ( 6, "José Benjamin Oliveira", "1956-04-23", "m", "" )]

class MainWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Test")
		self.set_border_width(10)

		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.add(vbox)

		stack = Gtk.Stack()

		# View 1: Pacient List
		self.grid1 = Gtk.Grid()
		self.grid1.set_column_homogeneous(True)
		self.grid1.set_row_homogeneous(True)
		stack.add_titled(self.grid1, "Pacient List", "Pacientes")

		#Creating the ListStore model
		#self.pacients_liststore = Gtk.ListStore(int, str, str, str, str)
		#for pacient in pacients_list:
			#self.pacients_liststore.append(list(pacient))

		#creating the treeview and adding the columns
		#self.treeview = Gtk.TreeView(self.pacients_liststore)
		#for i, column_title in enumerate(["Id", "Nome", "Data de Nascimento", "Sexo", "Observações"]):
			#renderer = Gtk.CellRendererText()
			#column = Gtk.TreeViewColumn(column_title, renderer, text=i)
			#self.treeview.append_column(column)

		#setting up the layout, putting the treeview in a scrollwindow, and the buttons in a row
		#self.scrollable_treelist = Gtk.ScrolledWindow()
		#self.scrollable_treelist.set_vexpand(True)
		#self.grid1.attach(self.scrollable_treelist, 0, 0, 8, 10)
		#self.scrollable_treelist.add(self.treeview)

		# View 2: Pacient Detail

		# Criar o formulário
		formBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		stack.add_titled(formBox, "Pacient Detail", "Detalhes")

		# Campo Nome
		nameLabel = Gtk.Label("Nome")
		formBox.pack_start(nameLabel, True, True, 0)
		nameEntry = Gtk.Entry()
		formBox.pack_start(nameEntry, True, True, 0)

		# Campo Data de Nascimento
		birthdayLabel = Gtk.Label("Data de Nascimento")
		formBox.pack_start(birthdayLabel, True, True, 0)
		birthdayEntry = Gtk.Entry()
		formBox.pack_start(birthdayEntry, True, True, 0)

		# Campo Sexo
		genderLabel = Gtk.Label("Sexo")
		formBox.pack_start(genderLabel, True, True, 0)
		genderBox = Gtk.Box(spacing=6)
		genderButtonMale = Gtk.RadioButton.new_with_label_from_widget(None, "Masculino")
		genderButtonFemale = Gtk.RadioButton.new_with_label_from_widget(genderButtonMale, "Feminino")
		genderBox.pack_start(genderButtonMale, True, True, 0)
		genderBox.pack_start(genderButtonFemale, True, True, 0)
		formBox.pack_start(genderBox, True, True, 0)

		# Campo Observações
		obsLabel = Gtk.Label("Observações")
		formBox.pack_start(obsLabel, True, True, 0)
		obsEntry = Gtk.Entry()
		formBox.pack_start(obsEntry, True, True, 0)

		# Botões
		buttonBox = Gtk.Box(spacing=6)
		saveButton = Gtk.Button.new_with_label("Salvar")
		cancelButton = Gtk.Button.new_with_label("Cancelar")
		buttonBox.pack_start(saveButton, True, True, 0)
		buttonBox.pack_start(cancelButton, True, True, 0)
		formBox.pack_start(buttonBox, True, True, 0)

		# View 3: Readings List
		self.grid3 = Gtk.Grid()
		self.grid3.set_column_homogeneous(True)
		self.grid3.set_row_homogeneous(True)
		stack.add_titled(self.grid3, "Readings List", "Readings")

		# View 4: Monitoring
		self.grid4 = Gtk.Grid()
		self.grid4.set_column_homogeneous(True)
		self.grid4.set_row_homogeneous(True)
		stack.add_titled(self.grid4, "Monitoring", "Monitoring")

		stack_switcher = Gtk.StackSwitcher()
		stack_switcher.set_stack(stack)
		vbox.pack_start(stack_switcher, True, True, 0)
		vbox.pack_start(stack, True, True, 0)

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
