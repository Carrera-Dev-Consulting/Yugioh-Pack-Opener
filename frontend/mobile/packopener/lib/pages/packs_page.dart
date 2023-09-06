import 'package:flutter/material.dart';
import 'package:packopener/widgets/packs/yugioh_pack.dart';


class PacksPage extends StatefulWidget {
  const PacksPage({super.key});

  @override
  State<PacksPage> createState() => _PackPageState();
}

class _PackPageState extends State<PacksPage> {
  @override
  Widget build(BuildContext context) {
    return const Scaffold(
        body: Center(
            child: YugiohPack()
            ));
  }
}
