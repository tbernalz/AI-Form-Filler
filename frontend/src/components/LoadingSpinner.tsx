import React from 'react';

const LoadingSpinner: React.FC = () => {
  return (
    <div
      id="loadingSpinner"
      className="flex justify-center items-center h-12 mt-3"
    >
      <div className="w-9 h-9 border-4 border-gray-200 border-t-blue-600 rounded-full animate-spin"></div>
    </div>
  );
};

export default LoadingSpinner;
