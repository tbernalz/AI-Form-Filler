import React, { useState } from 'react';
import LoadingSpinner from './LoadingSpinner';
import Waves from './Waves';

const TaxForm: React.FC = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [formData, setFormData] = useState({
    fullName: '',
    ssn: '',
    income: '',
    deductions: '',
    taxPaid: '',
    descriptions: '',
  });

  const typeEffect = (
    field: keyof typeof formData,
    value: string,
    delay: number
  ) => {
    let index = 0;

    const typeNextChar = () => {
      if (index < value.length) {
        setFormData((prev) => ({
          ...prev,
          [field]: value.slice(0, index + 1),
        }));
        index++;
        setTimeout(typeNextChar, delay);
      }
    };

    typeNextChar();
  };

  const autoFillTaxForm = async () => {
    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:8000/auto-fill-form', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error('Failed to auto-fill form');
      }

      const data = await response.json();
      console.log('Auto-filled data:', data);

      Object.keys(formData).forEach((key, index) => {
        setTimeout(
          () =>
            typeEffect(
              key as keyof typeof formData,
              data[key]?.toString() || '',
              100
            ),
          index * 1000
        );
      });
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setTimeout(
        () => setIsLoading(false),
        Object.keys(formData).length * 1000
      );
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100 p-5">
      <div className="max-w-md w-full bg-white p-5 rounded-lg shadow-md z-10">
        <h1 className="text-2xl font-bold text-center text-gray-800 mb-8">
          Tax Form
        </h1>
        <form className="space-y-4">
          <div>
            <label htmlFor="fullName" className="block text-base text-gray-700">
              Full Name
            </label>
            <input
              type="text"
              id="fullName"
              value={formData.fullName}
              name="fullName"
              readOnly
              className="w-full p-2.5 border border-gray-300 rounded-md text-base focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div>
            <label htmlFor="ssn" className="block text-base text-gray-700 mb-1">
              Social Security Number
            </label>
            <input
              type="text"
              id="ssn"
              value={formData.ssn}
              name="ssn"
              readOnly
              className="w-full p-2.5 border border-gray-300 rounded-md text-base focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div>
            <label
              htmlFor="income"
              className="block text-base text-gray-700 mb-1"
            >
              Annual Income
            </label>
            <input
              type="text"
              id="income"
              value={formData.income}
              name="income"
              readOnly
              className="w-full p-2.5 border border-gray-300 rounded-md text-base focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div>
            <label
              htmlFor="deductions"
              className="block text-base text-gray-700 mb-1"
            >
              Deductions
            </label>
            <input
              type="text"
              id="deductions"
              value={formData.deductions}
              name="deductions"
              readOnly
              className="w-full p-2.5 border border-gray-300 rounded-md text-base focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div>
            <label
              htmlFor="taxPaid"
              className="block text-base text-gray-700 mb-1"
            >
              Tax Already Paid
            </label>
            <input
              type="text"
              id="taxPaid"
              value={formData.taxPaid}
              name="taxPaid"
              readOnly
              className="w-full p-2.5 border border-gray-300 rounded-md text-base focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div>
            <label
              htmlFor="descriptions_request_for_extra_tax_return"
              className="block text-base text-gray-700 mb-1"
            >
              Any Further Information for Extra Tax Return
            </label>
            <textarea
              id="descriptions"
              value={formData.descriptions}
              rows={5}
              name="descriptions"
              readOnly
              className="w-full p-2.5 border border-gray-300 rounded-md text-base focus:outline-none focus:ring-2 focus:ring-blue-500"
            ></textarea>
          </div>

          <button
            type="button"
            onClick={autoFillTaxForm}
            className="w-full bg-blue-500 text-white py-2.5 px-5 rounded-md text-base hover:bg-blue-700 transition-colors"
            disabled={isLoading}
          >
            {isLoading ? 'Filling...' : 'AI Auto-Fill Tax Form'}
          </button>
        </form>

        {isLoading && <LoadingSpinner />}
      </div>
      <Waves />
    </div>
  );
};

export default TaxForm;
