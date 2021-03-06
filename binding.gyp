{
  'targets': [
    {
      'target_name': 'binding',
      'conditions': [
        ['OS=="mac"', {
          'sources': [
            'src/XpcConnection.cpp'
          ],
          # cflags on OS X are stupid and have to be defined like this
          'defines': [
            '_FILE_OFFSET_BITS=64',
            '_LARGEFILE_SOURCE'
          ],
          'xcode_settings': {
            'OTHER_CFLAGS': [
              '-Wall',
              '-ObjC++',
              '-Wdeprecated-declarations'
            ]
          }
        }]
      ],
      "include_dirs" : [
            "<!(node -e \"require('nan')\")"
        ]
    }
  ]
}
