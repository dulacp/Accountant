'use strict';

var gulp = require('gulp');
var runSequence = require('run-sequence');
var fs = require('fs');
var exec = require('child_process').exec;
var minimist = require('minimist');

// load plugins
var $ = require('gulp-load-plugins')();

// global config
var rootDir = 'accountant/';

// command line options
var knownOptions = {
    string: 'port',
    default: {
        port: '8000'
    }
};
var options = minimist(process.argv.slice(2), knownOptions);

gulp.task('styles', function () {
    return gulp.src(rootDir + 'assets/styles/accountant.scss')
        .pipe($.sass({
            outputStyle: 'expanded',
            precision: 10
        }))
        .pipe($.autoprefixer('last 1 version'))
        .pipe(gulp.dest(rootDir + 'assets/styles'))
        .pipe($.size())
        .pipe($.livereload());
});

gulp.task('scripts', function () {
    return gulp.src(rootDir + 'assets/scripts/**/*.js')
        .pipe($.jshint())
        .pipe($.jshint.reporter(require('jshint-stylish')))
        .pipe($.size())
        .pipe($.livereload());
});

gulp.task('compile', ['styles']);

gulp.task('clean', function () {
    return gulp.src(['.tmp'], { read: false }).pipe($.clean());
});

gulp.task('watch', function () {
    $.livereload.listen();

    // watch for changes

    gulp.watch([
        rootDir + 'templates/**/*.html',
        rootDir + 'assets/styles/**/*.css',
        rootDir + 'assets/scripts/**/*.js',
        rootDir + 'assets/images/**/*'
    ]);

    gulp.watch(rootDir + 'assets/styles/**/*.scss', ['styles']);
});

gulp.task('serve:backend', function() {
    var proc = exec('PYTHONUNBUFFERED=1 ./manage.py runserver ' + options.port);
    proc.stderr.on('data', function(data) { process.stdout.write(data); });
    proc.stdout.on('data', function(data) { process.stdout.write(data); });
});

gulp.task('launch', ['watch', 'compile', 'serve:backend']);

gulp.task('default', ['launch']);
