class YugiohCardDTO {
  final List<String> images;
  final String name;
  final String description;
  final String attribute;
  final String race;
  final int level;
  final int id;
  final String type;
  final int attack;
  final int defense;

  YugiohCardDTO(
      {required this.images,
      required this.name,
      required this.description,
      required this.attribute,
      required this.race,
      required this.level,
      required this.id,
      required this.attack,
      required this.defense,
      required this.type});

  factory YugiohCardDTO.fromJson(Map<String, dynamic> json) {
    List<String> images = List.empty(growable: true);
    var imagesBlob = json["card_images"][0] as Map<String, dynamic>;
    for (var entry in imagesBlob.entries) {
      images.add(entry.value);
    }
    return YugiohCardDTO(
        level: int.parse(json["level"].toString()),
        attribute: json["attribute"].toString(),
        attack: int.parse(json["attack"].toString()),
        defense: int.parse(json["defense"].toString()),
        name: json["name"].toString(),
        description: json["description"],
        type: json["type"].toString(),
        images: images,
        id: json["id"],
        race: json["race"]);
  }
}
