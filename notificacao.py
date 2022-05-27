from win10toast import ToastNotifier

#inicializa 
notificar = ToastNotifier()

#define parâmetros e mostra a notificação
notificar.show_toast(
"Notificação", "Testando as notificações", threaded=True, icon_path=None, duration=5
)