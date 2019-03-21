from questionset_service.encoder.mongo_serializer import JSONEncoder

from questionset_service.controller.base import BaseHandler


class QuestionHandler(BaseHandler):

    async def get(self, code):
        db = self.settings['db']
        question_doc = await db.question.find_one(
            {"code": code}
        )
        if question_doc:
            self.set_header("Access-Control-Allow-Origin", "*")
            self.write(JSONEncoder().encode(question_doc))
            return

        self.write_error(status_code=404)
