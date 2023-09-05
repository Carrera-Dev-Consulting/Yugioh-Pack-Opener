import 'package:flutter/widgets.dart';
import 'package:packopener/widgets/base/card_back.dart';
import 'package:packopener/widgets/base/card_front.dart';

// ignore: must_be_immutable
abstract class PlayingCard extends StatefulWidget {
  final double size;
  final CardFront front;
  final CardBack back;
  @override
  _FlippedState createState() => _FlippedState();
  const PlayingCard(
      {super.key, required this.front, required this.back, this.size = 1});
}

class _FlippedState extends State<PlayingCard> {
  bool flipped = false;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
        onTap: () => {
              setState(() {
                flipped = flipped ? false : true;
              })
            },
        child: Container(child: !flipped ? widget.front : widget.back));
  }
}
