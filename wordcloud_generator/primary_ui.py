import PySimpleGUI as psg

class PrimaryUI(psg.Window):

    GENERATE = 'Generate'

    def __init__(self):

        super().__init__('WordCloud Generator')

        self.txt_words = psg.Multiline(size=(25,5), do_not_clear=True)

        self.btn_generator = psg.Button(self.GENERATE)

        self.Layout(
            [
                [psg.Text('Input')],
                [self.txt_words],
                [self.btn_generator]
            ]
        )

    def start(self, generator_callback):

        while True:

            event, values = self.Read()

            print(event)

            if event is None: break

            elif event == self.GENERATE:

                # Generate Word Cloud

                input_text = self.txt_words.Get()

                generator_callback(input_text)

        self.Close()
