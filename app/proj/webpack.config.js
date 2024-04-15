let webpack = require('webpack');

const path = require('path');

const buildDirectory = 'ui/public/compiled';
// const filename = 'bundle.js';
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const TerserPlugin = require('terser-webpack-plugin');

module.exports = {
  entry: {
    example: ['./ui/exp-entry.js']
  },
  output: {
    path: path.join(__dirname, buildDirectory),
    filename: '[name].js',
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        },
      },
      {
        test: /\.scss$/,
        exclude: /node_modules/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          'sass-loader',
        ],
      },
    ],
  },
  plugins: [
    new MiniCssExtractPlugin({ filename: 'styles.css' }),
  ],
  watchOptions: {
    aggregateTimeout: 100,
    ignored: '/node_modules',
  },
  optimization: {
    minimize: true,
    minimizer: [new TerserPlugin()],
  },
};