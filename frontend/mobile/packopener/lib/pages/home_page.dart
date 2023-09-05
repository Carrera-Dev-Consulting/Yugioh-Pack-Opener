import 'package:flutter/material.dart';

import 'card_page.dart';

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Directionality(
        textDirection: TextDirection.ltr,
        child: Scaffold(
            backgroundColor: Theme.of(context).colorScheme.background,
            body: Center(
                //Added a shop button to better understand how flutter navigation works
                child: TextButton(
              child: const Text('Shop'),
              onPressed: () {
                Navigator.of(context).push(
                    MaterialPageRoute(builder: (context) => const CardPage()));
              },
            ))));
  }
}
