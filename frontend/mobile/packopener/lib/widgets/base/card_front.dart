
import 'package:flutter/material.dart';
import 'package:packopener/models/cards/card_model.dart';
import 'package:packopener/models/enums/game.dart';

abstract class CardFront extends StatefulWidget {
  final CardModel card;
  double size;
  final Game game;
  double width = 0;
  double height = 0;

  CardFront({super.key, this.size = 1, required this.card, required this.game}){
    var value = GameInfo.getSize(game);
    width = value["width"];
    height = value["height"];
  }
    @override
  // ignore: library_private_types_in_public_api
  _ExpandState createState() => _ExpandState();


}
class _ExpandState extends State<CardFront> {

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onLongPressStart: (details) => {
        setState(() {
          widget.size = widget.size*2;
        }),
      },

      onLongPressEnd: (details)=>{
        setState((){
          widget.size = widget.size/2;
        })
      },
      child: SizedBox(
        width: widget.size * widget.width,
        height: widget.size * widget.height,
        child: Image.network(widget.card.images[0])));
  }
}

