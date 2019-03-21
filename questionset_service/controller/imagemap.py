from questionset_service.encoder.mongo_serializer import JSONEncoder

from questionset_service.controller.base import BaseHandler


class ImageMapHandler(BaseHandler):

    async def get(self, question_code):
        db = self.settings['db']
        map_doc = await db.image_map.find_one(
            {"code": question_code}
        )
        if map_doc:
            self.set_header("Access-Control-Allow-Origin", "*")
            self.write(JSONEncoder().encode(map_doc))

        self.write_error(status_code=404)



