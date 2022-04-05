class InsideNodeDS:
    _name = None
    _value = None

    def __init__(self, name, value):
        self._name = name
        self._value = value

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    @name.setter
    def name(self, _name):
        self._name = _name

    @value.setter
    def value(self, _value):
        self._value = _value

    def __eq__(self, other):
        return self.name == other.name and self.value == other.value

    def __str__(self) -> str:
        print("Node name: {}, Node value: {}".format(self.name, self.value))
