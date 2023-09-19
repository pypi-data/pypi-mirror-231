#ifndef COORDINATESYSTEMWRAPPERBINDING_HPP
#define COORDINATESYSTEMWRAPPERBINDING_HPP

//pybind includes
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>
#include <pybind11/eigen.h>

#include "CoordinateSystemWrapper.hpp"
#include "geometry/curvilinear_coordinate_system.h"

namespace py = pybind11;

namespace plannerCPP
{

    void initBindCoordinateSystemWrapper(pybind11::module &m)
    {
        // TODO: Registering the CCS class is required for correct type signatures,
        // but we can't register the class here since it is also exported by commonroad_dc.
        // Registering it multiple times would result in pybind11 errors.
        // py::class_<geometry::CurvilinearCoordinateSystem, std::shared_ptr<geometry::CurvilinearCoordinateSystem>>(m, "_CurvilinearCoordinateSystem", py::module_local());

        py::class_<CoordinateSystemWrapper, std::shared_ptr<CoordinateSystemWrapper>>(m, "CoordinateSystemWrapper")
            .def(py::init<Eigen::Ref<RowMatrixXd>>(), py::arg("ref_path"))
            .def_property("system", &CoordinateSystemWrapper::getSystem, &CoordinateSystemWrapper::setSystem)
            .def_property("ref_pos",
                          [](CoordinateSystemWrapper &self) -> Eigen::Ref<Eigen::VectorXd> { return self.m_refPos;},
                          [](CoordinateSystemWrapper &self, const Eigen::Ref<const Eigen::VectorXd> arr) {self.m_refPos = arr;})
            .def_property("ref_curv",
                          [](CoordinateSystemWrapper &self) -> Eigen::Ref<Eigen::VectorXd> { return self.m_refCurv;},
                          [](CoordinateSystemWrapper &self, const Eigen::Ref<const Eigen::VectorXd> arr) {self.m_refCurv = arr;})
            .def_property("ref_theta",
                          [](CoordinateSystemWrapper &self) -> Eigen::Ref<Eigen::VectorXd> { return self.m_refTheta;},
                          [](CoordinateSystemWrapper &self, const Eigen::Ref<const Eigen::VectorXd> arr) {self.m_refTheta = arr;})
            .def_property("ref_curv_d",
                          [](CoordinateSystemWrapper &self) -> Eigen::Ref<Eigen::VectorXd> { return self.m_refCurvD;},
                          [](CoordinateSystemWrapper &self, const Eigen::Ref<const Eigen::VectorXd> arr) {self.m_refCurvD = arr;})
            .def_property("ref_curv_dd",
                          [](CoordinateSystemWrapper &self) -> Eigen::Ref<Eigen::VectorXd> { return self.m_refCurvDD;},
                          [](CoordinateSystemWrapper &self, const Eigen::Ref<const Eigen::VectorXd> arr) {self.m_refCurvDD = arr;})
            .def_readwrite("ref_line", &CoordinateSystemWrapper::m_refPolyLineFromCoordSys);

    }
} //plannerCPP

#endif //COORDINATESYSTEMWRAPPERBINDING_HPP