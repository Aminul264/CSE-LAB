import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  String url ="https://jsonplaceholder.typicode.com/users";
  getUser(url);
}
getUser(var apiURl) async {
  var res = await http.get(Uri.parse(apiURl));
  print(jsonDecode(res.body));
}
