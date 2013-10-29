module.exports = function(grunt) {

  'use strict';

  // Init config
  grunt.initConfig({
    jshint: {
      options: {
        jshintrc: '../.jshintrc',
        reporter: 'jshint'
      },
      all: [
        'lib/**/*.js',
        'public/js/**/*.js',
        '!public/js/vendor/**/*.js'
      ]
    }
  });

  // Jshint default task
  grunt.registerTask('default', ['jshint:all']);
  grunt.registerTask('ci', ['jshint:checkstyle']);
};
