var path = require("path")
var webpack = require('webpack')
var CopyWebpackPlugin = require('copy-webpack-plugin');
var ExtractTextPlugin = require("extract-text-webpack-plugin");
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  context: __dirname,

  devtool: 'source-map',

  entry: './assets/js/index.js',

  output: {
    path: path.resolve('./assets/bundles/'),
    filename: "[name]-[hash].js",
  },

  externals: {
    // require("jquery") is external and available on the global var jQuery
    "jquery": "jQuery",
    "jquery": "$"
  },

  plugins: [
    // Avoid publishing files when compilation failed:
    new webpack.NoEmitOnErrorsPlugin(),

    //optimizes webpack id order
    new webpack.optimize.OccurrenceOrderPlugin(),

    // Make webpack ignore moment locale require: https://github.com/moment/moment/issues/2517
    new webpack.IgnorePlugin(/^\.\/locale$/, /moment\/min$/),

    // global jquery is provided to any webpack modules
    new webpack.ProvidePlugin({
      $: "jquery",
      jQuery: "jquery",
      "window.jQuery": "jquery"
    }),

    //copy patternfly assets
    new CopyWebpackPlugin([
      {
        from: { glob:'./assets/html/*.html'},
        to: './',
        flatten: true
      },
      {
        from: { glob: './node_modules/patternfly/dist/img/*.*'},
        to: './img',
        flatten: true
      },
      {
        from: { glob: './node_modules/patternfly/dist/fonts/*.*'},
        to: './fonts',
        flatten: true
      },
      {
        from: { glob: './node_modules/patternfly/dist/css/*.*'},
        to: './css',
        flatten: true
      }
    ]),

    //creates distribution css file rather than inlining styles
    new ExtractTextPlugin("[name]-[hash].css", {allChunks: false}),

    // Track bundles for django-webpack-loader
    new BundleTracker({filename: './webpack-stats.json'}),
  ],

  module: {
    loaders: [
      // CSS loader
      {
        test: /\.css$/,
        loader: ExtractTextPlugin.extract({
          fallback: "style-loader",
          use: "css-loader?sourceMap"
        })
      },

      //font/image url loaders
      {
        test: /\.svg(\?v=\d+\.\d+\.\d+)?$/,
        loader: 'url-loader?limit=65000&mimetype=image/svg+xml&name=[name].[ext]'
      },
      {
        test: /\.(woff)(\?v=\d+\.\d+\.\d+)?$/,
        loader: 'url-loader?limit=65000&mimetype=application/font-woff&name=[name].[ext]'
      },
      {
        test: /\.(woff2)(\?v=\d+\.\d+\.\d+)?$/,
        loader: 'url-loader?limit=65000&mimetype=application/font-woff2&name=[name].[ext]'
      },
      {
        test: /\.ttf(\?v=\d+\.\d+\.\d+)?$/,
        loader: 'url-loader?limit=65000&mimetype=application/octet-stream&name=[name].[ext]'
      },
      {
        test:  /\.eot(\?v=\d+\.\d+\.\d+)?$/,
        loader: 'url-loader?limit=65000&mimetype=application/vnd.ms-fontobject&name[name].[ext]'
      },
      {
        test: /\.(png|jpe?g|gif)(\?\S*)?$/,
        loader: 'url-loader?limit=100000&name=[name].[ext]'
      }
    ]
  },
}