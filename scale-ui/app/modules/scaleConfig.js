(function () {
    'use strict';

    angular.module('scaleApp').service('scaleConfig', function (scaleConfigLocal) {

        var cfg = {
            colors: {
                emo_1: '#556270',
                    emo_2: '#4ecdc4',
                    emo_3: '#c7f464',
                    emo_4: '#ff6b6b',
                    emo_5: '#c44d58',

                    va_1: '#f2385a',
                    va_2: '#f5a503',
                    va_3: '#e9f1df',
                    va_4: '#4ad9d9',
                    va_5: '#3681bf',

                    df_1: '#566669',
                    df_2: '#bfe2ff',
                    df_3: '#0a131a',
                    df_4: '#122031',
                    df_5: '#00010d',

                    chart_blue: '#589ad0',
                    chart_gray: '#cccccc',
                    chart_gray_dark: '#aaaaaa',
                    chart_green: '#8fca0e',
                    chart_orange: '#ff7730',
                    chart_purple: '#bf81bf',
                    chart_red: '#f54d36',
                    chart_white: '#fff',
                    chart_yellow: '#ffc317',
                    chart_pink: '#fb03b2',

                    slate_blue_1: '#171C1C',
                    slate_blue_2: '#0F181C',

                    nav_bg: 'slate_blue_1',
                    nav_txt: 'light',

                    view_bg: 'light',
                    view_txt: '#434649',

                    accent_blue: 'va_5',

                    patternDefault: ['#4D4D4D','#5DA5DA','#FAA43A','#60BD68','#F17CB0','#B2912F','#B276B2','#DECF3F','#F15854'],
                    healthChart: ['#8fca0e', '#f54d36', '#ffc317', '#ff7730', '#3681bf', '#999999', '#d97bf9'],
                    statusChart: ['#999999', '#d97bf9', '#f54d36', '#ff7730', '#8fca0e', '#ffc317', '#3681bf'],
                    patternEmo: ['#556270','#4ecdc4','#c7f464','#ff6b6b','#c44d58'],
                    patternVa: ['#f2385a','#f5a503','#e9f1df','#4ad9d9','#3681bf'],
                    patternDf: ['#566669','#bfe2ff','#0a131a','#122031','#00010d'],
                    patternD320: ['#1f77bf','#aec7e8','#ff7f0e','#ffbb78','#2ca02c','#98df8a','#d62728','#ff9896','#9467bd','#c5b0d5','#8c564b','#c49c94','#e377c2','#f7b6d2','#7f7f7f','#c7c7c7','#bcbd22','#dbdb8d','#17becf','#9edae5']
            },

            queueThresholds: {
                success: 4,
                info: 8,
                warning: 12,
                danger: 16
            },

            jobTypes: [
                {id: 1, name: 'alfa', version: '1.0', title: 'alfa', icon: 'anchor', code: 'f13d'},
                {id: 2, name: 'bravo', version: '1.0', title: 'bravo', icon: 'bolt', code: 'f0e7'},
                {id: 3, name: 'charlie', version: '1.0', title: 'charlie', icon: 'bullseye', code: 'f140'},
                {id: 4, name: 'delta', version: '1.0', title: 'delta', icon: 'clock-o', code: 'f017'},
                {id: 5, name: 'echo', version: '1.0', title: 'echo', icon: 'cloud', code: 'f0c2'},
                {id: 6, name: 'foxtrot', version: '1.0', title: 'foxtrot', icon: 'compass', code: 'f14e'},
                {id: 7, name: 'golf', version: '1.0', title: 'golf', icon: 'crosshairs', code: 'f05b'},
                {id: 8, name: 'hotel', version: '1.0', title: 'hotel', icon: 'database', code: 'f1c0'},
                {id: 9, name: 'india', version: '1.0', title: 'india', icon: 'diamond', code: 'f219'},
                {id: 10, name: 'juliet', version: '1.0', title: 'juliet', icon: 'eye', code: 'f06e'},
                {id: 11, name: 'kilo', version: '1.0', title: 'kilo', icon: 'fighter-jet', code: 'f0fb'},
                {id: 12, name: 'lima', version: '1.0', title: 'lima', icon: 'picture-o', code: 'f1c5'},
                {id: 13, name: 'mike', version: '1.0', title: 'mike', icon: 'fire', code: 'f06d'},
                {id: 14, name: 'november', version: '1.0', title: 'november', icon: 'gavel', code: 'f0e3'},
                {id: 15, name: 'oscar', version: '1.0', title: 'oscar', icon: 'globe', code: 'f0ac'},
                {id: 16, name: 'papa', version: '1.0', title: 'papa', icon: 'key', code: 'f11c'},
                {id: 17, name: 'quebec', version: '1.0', title: 'quebec', icon: 'male', code: 'f183'},
                {id: 18, name: 'romeo', version: '1.0', title: 'romeo', icon: 'moon-o', code: 'f186'},
                {id: 19, name: 'sierra', version: '1.0', title: 'sierra', icon: 'paw', code: 'f1b0'},
                {id: 20, name: 'tango', version: '1.0', title: 'tango', icon: 'recycle', code: 'f1b8'},
                {id: 21, name: 'uniform', version: '1.0', title: 'uniform', icon: 'shield', code: 'f132'},
                {id: 22, name: 'victor', version: '1.0', title: 'victor', icon: 'tachometer', code: 'f0e4'},
                {id: 23, name: 'whiskey', version: '1.0', title: 'whiskey', icon: 'umbrella', code: 'f0e9'},
                {id: 24, name: 'xray', version: '1.0', title: 'xray', icon: 'file-o', code: 'f016'},
                {id: 25, name: 'alfa2', version: '1.0', title: 'alfa2', icon: 'anchor', code: 'f13d'},
                {id: 26, name: 'bravo2', version: '1.0', title: 'bravo2', icon: 'bolt', code: 'f0e7'},
                {id: 27, name: 'charlie2', version: '1.0', title: 'charlie2', icon: 'bullseye', code: 'f140'},
                {id: 28, name: 'delta2', version: '1.0', title: 'delta2', icon: 'clock-o', code: 'f017'},
                {id: 29, name: 'echo2', version: '1.0', title: 'echo2', icon: 'cloud', code: 'f0c2'},
                {id: 30, name: 'foxtrot2', version: '1.0', title: 'foxtrot2', icon: 'compass', code: 'f14e'},
                {id: 31, name: 'golf2', version: '1.0', title: 'golf2', icon: 'crosshairs', code: 'f05b'},
                {id: 32, name: 'hotel2', version: '1.0', title: 'hotel2', icon: 'database', code: 'f1c0'},
                {id: 33, name: 'india2', version: '1.0', title: 'india2', icon: 'diamond', code: 'f219'},
                {id: 34, name: 'juliet2', version: '1.0', title: 'juliet2', icon: 'eye', code: 'f06e'},
                {id: 35, name: 'kilo2', version: '1.0', title: 'kilo2', icon: 'fighter-jet', code: 'f0fb'},
                {id: 36, name: 'lima2', version: '1.0', title: 'lima2', icon: 'picture-o', code: 'f1c5'},
                {id: 37, name: 'mike2', version: '1.0', title: 'mike2', icon: 'fire', code: 'f06d'},
                {id: 38, name: 'november2', version: '1.0', title: 'november2', icon: 'gavel', code: 'f0e3'},
                {id: 39, name: 'oscar2', version: '1.0', title: 'oscar2', icon: 'globe', code: 'f0ac'},
                {id: 40, name: 'papa2', version: '1.0', title: 'papa2', icon: 'key', code: 'f11c'}
            ],

            mediaTypes: [
                {mimeType: 'text/csv', icon: 'fa-file-excel-o'},
                {mimeType: 'text/plain', icon: 'fa-file-text-o'},
                {mimeType: 'application/zip', icon: 'fa-file-archive-o'},
                {mimeType: 'application/json', icon: 'fa-file-code-o'},
                {mimeType: 'application/xml', icon: 'fa-file-excel-o'},
                {mimeType: 'application/vnd.geo+json', icon: 'fa-file-code-o'},
                {mimeType: 'application/vnd.google-earth.kml+xml', icon: 'fa-globe'},
                {mimeType: 'application/vnd.google-earth.kmz', icon: 'fa-globe'},
                {mimeType: 'image/png', icon: 'fa-file-image-o'},
                {mimeType: 'image/x-hdf5-image', icon: 'fa-file-image-o'},
                {mimeType: 'image/x-nitf-image', icon: 'fa-file-image-o'},
                {mimeType: 'image/tiff', icon: 'fa-file-image-o'},
                {mimeType: 'video/avi', icon: 'fa-file-video-o'},
                {mimeType: 'video/mp4', icon: 'fa-file-video-o'}
            ],

            triggerTypes: ['PARSE', 'INGEST'],

            taskStatusStyles: {
                "SUCCEEDED" : "bar",
                "FAILED" : "bar-failed",
                "RUNNING" : "bar-running",
                "KILLED" : "bar-killed"
            },

            dateFormats: {
                "day": "YYYY-MM-DD",
                "day_hour": "YYYY-MM-DD HHZ",
                "day_minute": "YYYY-MM-DD HH:MM",
                "day_minute_utc": "YYYY-MM-DD HH:MM[Z]",
                "day_second": "YYYY-MM-DD HH:MM:SSZ",
                "day_second_utc": "YYYY-MM-DD HH:MM:SS[Z]",
                "day_millis": 'YYYY-MM-DD HH:mm:ss.SSS',
                "hour_minute": "HH:mm",
                "hour_seconds": "HH:mm:ss",
                "duration_hm": "HH:mm",
                "duration_hms": "HH:mm:ss"

            },

            jobStatus: ['VIEW ALL','COMPLETED','BLOCKED','QUEUED','RUNNING','FAILED','CANCELED','PENDING'],

            ingestStatus: ['VIEW ALL','TRANSFERRING','TRANSFERRED','DEFERRED','INGESTING','INGESTED','ERRORED','DUPLICATE'],

            axisTypes: ['linear', 'time'],

            executions: ['success','warning','error'],

            defaultIcon: 'gear',

            defaultIconCode: 'f013',

            activityIconCode: 'f110',

            urls: {
                prefixDev: 'http://127.0.0.1:9000/', // dev
                prefixProd: 'http://127.0.0.1:9000/',
                documentation: '/docs',

                getQueueStatus: function () {
                    return this.prefixProd + 'queue/status/';
                },
                getQueueDepth: function (started, ended) {
                    return this.prefixProd + 'queue/depth/?started=' + started + '&ended=' + ended;
                },
                requeueJob: function () {
                    return this.prefixProd + 'queue/requeue-job/'
                },
                getRecipeTypes: function () {
                    return this.prefixProd + 'recipe-types/';
                },
                saveRecipeType: function () {
                    return this.getRecipeTypes();
                },
                validateRecipeType: function () {
                    return this.prefixProd + 'recipe-types/validation/';
                },
                getRecipeTypeDetail: function (id) {
                    return this.prefixProd + 'recipe-types/' + id + '/';
                },
                getRecipes: function () {
                    return this.prefixProd + 'recipes/';
                },
                getRecipeDetails: function (id) {
                    return this.prefixProd + 'recipes/' + id + '/';
                },
                getJobs: function () {
                    return this.prefixProd + 'jobs/';
                },
                updateJob: function (id) {
                    return this.prefixProd + 'jobs/' + id + '/';
                },
                getRunningJobs: function () {
                    return this.prefixProd + 'job-types/running/';
                },
                getJobTypes: function () {
                    return this.prefixProd + 'job-types/';
                },
                getJobTypeStatus: function () {
                    return this.prefixProd + 'job-types/status/';
                },
                getJobTypeDetails: function (id) {
                    return this.prefixProd + 'job-types/' + id + '/';
                },
                updateJobType: function (id) {
                    return this.prefixProd + 'job-types/' + id + '/';
                },
                getJobDetail: function (id) {
                    return this.prefixProd + 'jobs/' + id + '/';
                },
                getJobExecutions: function () {
                    return this.prefixProd + 'job-executions/';
                },
                getJobExecutionLog: function (execId) {
                    return this.prefixProd + 'job-executions/' + execId + '/logs/';
                },
                getJobExecutionDetails: function (execId) {
                    return this.prefixProd + 'job-executions/' + execId + '/';
                },
                getMetricsDataTypes: function () {
                    return this.prefixProd + 'metrics/';
                },
                getMetricsDataTypeOptions: function (name) {
                    return this.prefixProd + 'metrics/' + name + '/';
                },
                getMetricsPlotData: function (name) {
                    return this.prefixProd + 'metrics/' + name + '/plot-data/';
                },
                getNodes: function () {
                    return this.prefixProd + 'nodes/';
                },
                getNode: function (slaveId) {
                    return this.prefixProd + 'nodes/' + slaveId + '/';
                },
                getNodeStatus: function () {
                    return this.prefixProd + 'nodes/status/';
                },
                updateNode: function (id) {
                    return this.prefixProd + 'nodes/' + id + '/';
                },
                getStatus: function () {
                    return this.prefixProd + 'status/';
                },
                getJobLoad: function () {
                    return this.prefixProd + 'load/';
                },
                getDataFeed: function() {
                    return this.prefixProd + 'ingests/status/';
                },
                getIngests: function(){
                    return this.prefixProd + 'ingests/';
                },
                updateScheduler: function () {
                    return this.prefixProd + 'scheduler/';
                },
                getWorkspaces: function() {
                    return this.prefixProd + 'workspaces/';
                }
            },
            defaultGaugeWidth: 160,
            pollIntervals: {
                // minutes * (seconds * milliseconds)
                runningJobs: 5 * (60 * 1000),
                jobs: 5 * (60 * 1000),
                jobTypes: 5 * (60 * 1000),
                jobExecutionLog: 5 * (60 * 1000),
                jobTypeStatus: 5 * (60 * 1000),
                nodes: 5 * (60 * 1000),
                nodeStatus: 5 * (60 * 1000),
                queueStatus: 5 * (60 * 1000),
                queueDepth: 5 * (60 * 1000),
                status: 5 * (60 * 1000),
                jobLoad: 5 * (60 * 1000)
            },
            subnavLinks: {
                jobs: [
                    { path: 'jobs', label: 'Jobs' },
                    { path: 'jobs/types', label: 'Job Types' }
                ],
                load: [
                    { path: 'load', label: 'Queued' },
                    { path: 'load/running', label: 'Running' },
                    { path: 'load/depth', label: 'Job Load' }
                ],
                recipes: [
                    { path: 'recipes', label: 'Recipes' },
                    { path: 'recipes/types', label: 'Recipe Types' }
                ],
                feed: [
                    { path: 'feed', label: 'Status' },
                    { path: 'feed/ingests', label: 'Ingest Records' }
                ]
            },
            headerOffset: 160
        };
        _.merge(cfg, scaleConfigLocal);
        return cfg;
    });
})();
