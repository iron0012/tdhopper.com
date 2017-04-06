var gulp = require('gulp')
var htmlmin = require('gulp-htmlmin');
var htmllint = require('gulp-htmllint');
var gutil = require('gulp-util');

gulp.task('lint', function(){
    return gulp.src('output/*')
        .pipe(htmllint({}, htmllintReporter));
});

gulp.task('copy', function() {
    return gulp.src(['./output/**', '!./output/**/**.html'])
        .pipe(gulp.dest('dist'));
});

gulp.task('html', function() {
    return gulp.src('./output/**/*.html')
        .pipe(htmlmin({
            collapseWhitespace: true
        }))
        .pipe(gulp.dest('dist'));
});

gulp.task('default', ['copy', 'html']);

function htmllintReporter(filepath, issues) {
    if (issues.length > 0) {
        issues.forEach(function (issue) {
            gutil.log(gutil.colors.cyan('[gulp-htmllint] ') + gutil.colors.white(filepath + ' [' + issue.line + ',' + issue.column + ']: ') + gutil.colors.red('(' + issue.code + ') ' + issue.msg));
        });

        process.exitCode = 1;
    }
}
