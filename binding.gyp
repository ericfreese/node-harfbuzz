{
  "targets": [
    {
      "target_name": "addon",
      "sources": [
        "src/harfbuzz.cc",
      ],
      "include_dirs": ["<!(node -e \"require('nan')\")", "node_modules/freetype2/src", "/usr/local/include/freetype2", "/usr/local/include/harfbuzz"],
      "libraries": [ "-lfreetype", "-lharfbuzz" ]
    }
  ]
}
