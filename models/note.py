class Note:
    def __init__(self, title, content, urgency, date):
        self.title = title
        self.content = content
        self.urgency = urgency
        self.date = date

    def to_dict(self):
        return {
            'title': self.title,
            'content': self.content,
            'urgency': self.urgency,
            'date': self.date
        }
