import 'package:packopener/widgets/cards/constants.dart';

enum Game { yugioh, pokemon, magic, other }
abstract class GameInfo{
  static dynamic getSize(Game game){
    var size;
    switch(game){
      case Game.yugioh:
      size = {"width":YugiohConstants.CARD_WIDTH, "height":YugiohConstants.CARD_HEIGHT};
      break;
      case Game.other:
      size = {"width":BaseCard.CARD_WIDTH, "height":BaseCard.CARD_HEIGHT};
      break;
      default:
      throw Exception("The game you have chosen has not been implemented yet");      
    }
    return size;
  }
}