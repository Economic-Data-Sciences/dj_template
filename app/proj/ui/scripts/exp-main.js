import React from 'react';
import { createRoot } from 'react-dom/client';
import Example from './components/exp-comp';

const container = document.getElementById('jsHolder');
const root = createRoot(container);
root.render(<Example />);
