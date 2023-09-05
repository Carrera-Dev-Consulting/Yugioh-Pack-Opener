import 'package:flutter/material.dart';
import "package:flutter/services.dart";
import 'package:packopener/pages/home_page.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  SystemChrome.setPreferredOrientations(
          [DeviceOrientation.landscapeLeft, DeviceOrientation.landscapeRight])
      .then((value) {
    //Removes the notification bar on your device to full scren the device
    SystemChrome.setEnabledSystemUIMode(SystemUiMode.immersiveSticky);
    SystemChrome.setSystemUIOverlayStyle(const SystemUiOverlayStyle(
        statusBarColor: Colors.transparent,
        systemNavigationBarColor: Colors.transparent));
    //Whenever there is a system ui change make sure to close the system ui to keep the app fullscreened
    SystemChrome.setSystemUIChangeCallback((systemOverlaysAreVisible) {
      return SystemChrome.setEnabledSystemUIMode(SystemUiMode.immersiveSticky);
    });
    runApp(const MyApp());
  });
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Pack Opener',
      theme: ThemeData(
        colorScheme: const ColorScheme(
          brightness: Brightness.dark,
          background: Color.fromARGB(255, 41, 47, 54),
          primary: Color.fromARGB(255, 78, 205, 196),
          secondary: Color.fromARGB(255, 247, 255, 247),
          tertiary: Color.fromARGB(255, 255, 107, 107),
          onBackground: Color.fromARGB(255, 247, 255, 247),
          error: Color.fromARGB(255, 41, 47, 54),
          onError: Color.fromARGB(255, 255, 107, 107),
          onPrimary: Color.fromARGB(255, 247, 255, 247),
          onSecondary: Color.fromARGB(255, 41, 47, 54),
          onSurface: Color.fromARGB(255, 41, 47, 54),
          surface: Color.fromARGB(255, 78, 205, 196),
        ),
        useMaterial3: true,
      ),
      home: const SafeArea(
          left: false,
          bottom: false,
          right: false,
          top: false,
          child: MyHomePage()),
    );
  }
}
