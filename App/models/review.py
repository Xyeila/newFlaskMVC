from App.database import db

class Review(db.Model):
    reviewId = db.Column(db.Integer, primary_key=True, nullable=False) 
    userId = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    studentId = db.Column(db.Integer, db.ForeignKey('Student.studentId'), nullable=False)
    comment = db.Column(db.String)
    like = db.Column(db.Integer, nullable=False)
    dislike = db.Column(db.Integer, nullable=False)
        
    def __init__(self, reviewId):
        self.reviewId = reviewId
    

    def toJSON(self):
        return{
            'reviewId' = reviewId
        }

    
    

