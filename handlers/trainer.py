from tornado.web import asynchronous
from handlers.base import BaseHandler
import simplejson as json


class TrainerInfoHandler(BaseHandler):

    @asynchronous
    def get(self):
        # Get trainer with email and write that JSON
        curr_trainer = json.loads(self.get_current_user())

        get_trainer = """SELECT * FROM `Trainer` WHERE `trainer_email` = "%s" """\
                        % (curr_trainer['email'])
        trainer = self.application.db.get(get_trainer)
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(trainer))
        self.finish()


class TrainerSignupHandler(BaseHandler):

    @asynchronous
    def post(self):
        curr_user = json.loads(self.get_current_user())
        name = curr_user["name"]
        email = curr_user["email"]

        body = json.loads(self.request.body)
        trainer = body["trainer"]
        trainer["name"] = name
        trainer["email"] = email

        if self.add_trainer(trainer):
            self.write({"success": "true"})
        else:
            self.write({"success": "false"})
        self.finish()

    def add_trainer(self, trainer):
        add_trainer_info = """INSERT INTO `Trainer` (`trainer_name`, `trainer_email`, `gym`, `certification`) VALUES ("%s", "%s", "%s", "%s")"""\
                        % (trainer["name"], trainer["email"], trainer["gym"], trainer["certification"])
        result = self.application.db.execute(add_trainer_info)

        return True if result is not None else False
