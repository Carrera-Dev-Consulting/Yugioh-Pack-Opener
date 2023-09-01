import 'package:packopener/controllers/json_dummy_reader.dart';
import 'package:packopener/models/dto/yugioh_card_dto.dart';

class YugiohDataReader {
  static Future<List<YugiohCardDTO>> readJson() async {
    var json = await JsonDummyReader.readJson();
    var rest = json["cards"] as List;
    var list =
        rest.map<YugiohCardDTO>((e) => YugiohCardDTO.fromJson(e)).toList();
    return list;
  }
}
