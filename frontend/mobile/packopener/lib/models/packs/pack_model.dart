// import 'package:packopener/models/cards/card_model.dart';
// import 'package:packopener/models/enums/game.dart';

// class PackModel {
//   final List<CardModel> cards;
//   final int price;
//   final String images;

//   factory PackModel.fromJson(Map<String, dynamic> json) {
//     dynamic cardblobs = json["cards"];
//     for (int i = 0; i < cardblobs.length; i++) {}
//     List<String> images = List.empty(growable: true);
//     for (var i = 0; i < cardblobs["card_images"].length; i++) {
//       images.add(cardblobs["card_images"][i]["image_url"].toString());
//       images.add(cardblobs["card_images"][i]["image_url_small"].toString());
//     }

//     return YugiohCardModel(
//         level: int.parse(cardblobs["level"].toString()),
//         attribute: cardblobs["attribute"].toString(),
//         attack: int.parse(cardblobs["attack"].toString()),
//         defense: int.parse(cardblobs["defense"].toString()),
//         name: cardblobs["name"].toString(),
//         description: cardblobs["description"],
//         type: cardblobs["type"].toString(),
//         images: images);
//   }
// }
