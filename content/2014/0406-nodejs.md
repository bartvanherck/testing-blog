title: Nodejs
tags: nodejs
date: 2014-04-06 00:21:00
category: web, testing
Summary: Today I am doing some end-to-end testing of a frontend. That frontend is made in angularjs. The features of this application is, that it has to be generic to fit in several other projects.

Today I am doing some end-to-end testing of a frontend. That frontend is made in angularjs. The features of this application is, that it has to be generic to fit in several other projects.

This means it is a kind of framework. Because the back-end for the different applications can have some hardware, it is time to mock the hardware. But mocking, is that an end-to-end test? Because I think it is not, I wrote a kind of a simulator. The simulator will mimic the backend that we use. I decided to write that back-end in javascript to learn how to create a nodeJs application.  First an environment has to be setup.

The environment will contain tests and source code. Lucky we can make use of the grunt tool. And testing will be done in jasmine. As simple as that.

What do we need? A file that is called package.json. This file describes the application. There are several features in it, like project name, description, dependencies and version number.  A basic template we use is here:

<code class="javascript"><pre>
{
    "name": "simulator",
    "version": "0.0.1",
    "description": "A nodeJs app for simulation of the backend",
    "main": "backend.js",
    "dependencies": {
        "ws": "~0.4.31"
    },
    "devDependencies": {
        "grunt": "~0.4.2",
        "grunt-contrib-watch": "~0.5.3", 
        "grunt-jasmine-node": "~0.1.0",
        "grunt-contrib-jshint": "~0.8.0", 
        "grunt-jasmine-node-coverage": "~0.1.7", 
        "grunt-exec": "~0.4.5" 
    }, 
    "scripts": { 
        "test": "test" 
    }, 
    "author": "Bart Vanherck", 
    "license": "GPL" 
}
</pre></code>

As you can see, in devDependencies are all dependencies to run the grunt tool and in dependencies, the dependencies of the application are listed. After creation of this file, a &nbsp;Gruntfile.js needs to be created. This file contains the tasks grunt can do.

Example: (GRUNTFILE.js) 
<code class="javascript"><pre>
{
    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON("package.json"),
 
        watch: {
            files: ["Gruntfile.js","spec/*.spec.js", "src/*.js"],
            tasks: ["jshint", "jasmine_node"],
       },
 
       jshint: {
           options: {
               unused: true,
               trailing: true,
               noempty: true,
               curly: true,
               indent: 4
           },
           all: ["Gruntfile.js", "src/*.js", "spec/*.spec.js"]
        },
 
        jasmine_node: {
            coverage: {
                showColors:true
            },
            options: {
                forceExit: true,
                match: ".",
                matchall: false,
                extensions: "js",
                specNameMatcher: "spec",
                junitreport: {
                    report: true,
                    savePath : "./coverage/reports/",
                    useDotNotation: true,
                    consolidate: false
                }
             }
        },
        exec: {
            toHtml: {
                command: "istanbul report html"
            }
        }
    });
 
    grunt.loadNpmTasks("grunt-contrib-watch");
    grunt.loadNpmTasks("grunt-jasmine-node");
    grunt.loadNpmTasks("grunt-contrib-jshint");
    grunt.loadNpmTasks("grunt-jasmine-node-coverage");
    grunt.loadNpmTasks("grunt-exec");
 
    grunt.registerTask("coverage", "jasmine_node");
    grunt.registerTask("test", "jasmine_node");
    grunt.registerTask("tohtml", "exec:toHtml");
    grunt.registerTask("default", "test");};
</pre></code>

After creation of the files, the real application can be build. This however is for a next time.
