import React, { useState } from 'react';
import LoadingSpinner from './LoadingSpinner';
import Waves from './Waves';

const TaxForm: React.FC = () => {
  const [isLoading, setIsLoading] = useState(false);

  const autoFillTaxForm = () => {
    setIsLoading(true);
    // API call - pending
    setTimeout(() => {
      setIsLoading(false);
    }, 2000);
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100 p-5">
      <Waves />
      <div className="max-w-md w-full bg-white p-5 rounded-lg shadow-md z-10">
        <h1 className="text-2xl font-bold text-center text-gray-800 mb-8">
          Simple Tax Return Form
        </h1>
        <form className="space-y-4">
          <div>
            <label htmlFor="fullName" className="block text-base text-gray-700">
              Full Name:
            </label>
            <input
              type="text"
              id="fullName"
              name="fullName"
              className="w-full p-2.5 border border-gray-300 rounded-md text-base focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div>
            <label htmlFor="ssn" className="block text-base text-gray-700 mb-1">
              Social Security Number:
            </label>
            <input
              type="text"
              id="ssn"
              name="ssn"
              className="w-full p-2.5 border border-gray-300 rounded-md text-base focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div>
            <label
              htmlFor="income"
              className="block text-base text-gray-700 mb-1"
            >
              Annual Income:
            </label>
            <input
              type="text"
              id="income"
              name="income"
              className="w-full p-2.5 border border-gray-300 rounded-md text-base focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div>
            <label
              htmlFor="deductions"
              className="block text-base text-gray-700 mb-1"
            >
              Deductions:
            </label>
            <input
              type="text"
              id="deductions"
              name="deductions"
              className="w-full p-2.5 border border-gray-300 rounded-md text-base focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div>
            <label
              htmlFor="taxPaid"
              className="block text-base text-gray-700 mb-1"
            >
              Tax Already Paid:
            </label>
            <input
              type="text"
              id="taxPaid"
              name="taxPaid"
              className="w-full p-2.5 border border-gray-300 rounded-md text-base focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div>
            <label
              htmlFor="descriptions_request_for_extra_tax_return"
              className="block text-base text-gray-700 mb-1"
            >
              Any Further Information for Extra Tax Return:
            </label>
            <textarea
              id="descriptions_request_for_extra_tax_return"
              name="descriptions_request_for_extra_tax_return"
              rows={5}
              className="w-full p-2.5 border border-gray-300 rounded-md text-base focus:outline-none focus:ring-2 focus:ring-blue-500"
            ></textarea>
          </div>

          <button
            type="button"
            onClick={autoFillTaxForm}
            className="w-full bg-blue-500 text-white py-2.5 px-5 rounded-md text-base hover:bg-blue-700 transition-colors"
          >
            AI Auto-Fill Tax Form
          </button>
        </form>

        {isLoading && <LoadingSpinner />}
      </div>
    </div>
  );
};

export default TaxForm;
