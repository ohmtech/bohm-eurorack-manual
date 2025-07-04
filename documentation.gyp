##############################################################################
#
#     documentation.gyp
#     Copyright (c) 2024 Raphael DINGE
#
#Tab=3########################################################################



{
   'targets' : [
      {
         'target_name': 'documentation',
         'type': 'none',

         'sources': [
            'README.md',
            'index.md',

            'installation/index.md',
            'installation/expanders.jpg',
            'installation/power.jpg',

            'specifications/index.md',

            'overview/index.md',
            'overview/outline-bohm.svg',
            'overview/outline-groove.svg',
            'overview/outline-performer.svg',

            'functions/index.md',
            'functions/routing.svg',
            'functions/bohm.svg',
            'functions/groove.svg',
            'functions/performer.svg',

            'library/index.md',

            'modes/index.md',
            'modes/snapshot.svg',
            'modes/song-mode.svg',
            'modes/jam-mode.svg',
            'modes/studio.svg',

            'system/index.md',
            'update/index.md',
            'calibration/index.md',
            'factory/index.md',
            'changelog/index.md',
            'licenses/index.md',
            'thanks/index.md',
         ],
      },
   ],
}
